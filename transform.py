# Extract data to pandas dataframe
import pandas as pd

def transform_weather_data(retrieved_data):
    weather_data = []
    for data in retrieved_data["list"]:
        weather_data.append({
            'datetime': data['dt_txt'],
            'temperature': data['main']['temp'],
            'human_temp_feel': data['main']['feels_like'],
            'min_temp': data['main']['temp_min'],
            'max_temp': data['main']['temp_max'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'] * 3.6
        })
    return pd.DataFrame(weather_data)
