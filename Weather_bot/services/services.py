import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": city,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        return f"Weather in {city}: {data['current']['temperature']}°C, {data['current']['weather_descriptions'][0]}"
    else:
        return "ERROR"
