import requests
from config import API_KEY, API_URL, LOCATION

def extract_weather_data():
    params = {
        "appid": API_KEY,
        "lat": LOCATION["latitude"],
        "lon": LOCATION["longitude"],
        "units": "metric"
    }

    response = requests.get(url=API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")
