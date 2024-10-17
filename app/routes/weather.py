from fastapi import APIRouter, Depends, HTTPException
from app.utils.jwt_handler import get_current_user
from app.utils.weather_scraper import get_weather_data, process_weather_data

router = APIRouter(tags=["Weather"])


@router.get("/consultar/")
async def consultar_clima(current_user: dict = Depends(get_current_user)):
    data = get_weather_data()
    if data:
        forecast = process_weather_data(data)
        return {"previsao": forecast}
    else:
        raise HTTPException(status_code=500, detail="Erro ao obter os dados do clima")
