import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather_data():
    api_key = "127584e87c347080f9081e49dde5cafe"

    if not api_key:
        print("Chave de API não encontrada. Verifique se ela está definida nas variáveis de ambiente.")
        return None

    city_id = '3448439'  # ID de São Paulo, Brasil
    url = f'http://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}&lang=pt_br&units=metric'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data  # Retornamos o JSON bruto
    else:
        print(f'Erro ao acessar a API: {response.status_code}')
        return None


def process_weather_data(data):
    forecast = {}

    for item in data['list']:
        date_text = item['dt_txt']  # Exemplo: '2024-10-15 00:00:00'
        date = date_text.split(' ')[0]  # Obter apenas a data, sem o horário

        temp = item['main']['temp']
        description = item['weather'][0]['description']

        if date not in forecast:
            forecast[date] = {
                'temperaturas': [],
                'descricoes': []
            }

        forecast[date]['temperaturas'].append(temp)
        forecast[date]['descricoes'].append(description)

    # Agora, vamos calcular a temperatura mínima, máxima e a descrição mais comum para cada dia
    formatted_forecast = []
    for date, info in forecast.items():
        min_temp = min(info['temperaturas'])
        max_temp = max(info['temperaturas'])
        # Selecionar a descrição mais frequente
        description = max(set(info['descricoes']), key=info['descricoes'].count)
        formatted_forecast.append({
            'data': date,
            'temperatura_minima': round(min_temp, 2),
            'temperatura_maxima': round(max_temp, 2),
            'descricao': description
        })

    # Ordenar a lista de previsões por data
    formatted_forecast.sort(key=lambda x: x['data'])

    return formatted_forecast

