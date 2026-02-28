from fastapi import FastAPI
from mangum import Mangum
from .routes import router
from .config import settings
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)

handler = Mangum(app)