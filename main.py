# main.py

from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.weather import router as weather_router

app = FastAPI()

app.include_router(user_router)
app.include_router(weather_router)
