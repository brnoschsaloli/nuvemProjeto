# main.py

from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.weather import router as weather_router
from app.database import engine
from app.models import Base

app = FastAPI()

app.include_router(user_router)
app.include_router(weather_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tabelas criadas ou já existentes.")
