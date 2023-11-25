import requests
from opencage.geocoder import OpenCageGeocode
from config.config import Config, load_config
from lexicon.lexicon import LEXICON_EMODJI
config: Config = load_config()
api_key_geo = config.Weather_bot.api_key_geo
api_key = config.Weather_bot.api_key

def get_weather_city(city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": city,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        return f"Погода в {city}: {data['current']['temperature']}°C🌡️, {data['current']['weather_descriptions'][0]}{LEXICON_EMODJI[data['current']['weather_descriptions'][0]]}"
    else:
        return "ERROR"

def get_weather_geo(latitude, longitude):
    base_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={latitude},{longitude}"
    response = requests.get(base_url)
    data = response.json()
    city = process_get_city(latitude, longitude)
    if response.status_code == 200:
        return f"Погода в {city}: {data['current']['temperature']}°C🌡️, {data['current']['weather_descriptions'][0]}{LEXICON_EMODJI[data['current']['weather_descriptions'][0]]}"
    else:
        return "ERROR"

def process_get_city(latitude, longitude):
    geocoder = OpenCageGeocode(api_key_geo)
    result = geocoder.reverse_geocode(latitude, longitude)
    city_name = result[0]['components']['city']
    return city_name
