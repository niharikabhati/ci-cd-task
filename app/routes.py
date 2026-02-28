from fastapi import APIRouter, HTTPException
from .models import tasks_db
from .schemas import Task, TaskCreate

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    task_id = len(tasks_db) + 1
    new_task = {"id": task_id, **task.dict()}
    tasks_db.append(new_task)
    return new_task

@router.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks_db

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            tasks_db.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")