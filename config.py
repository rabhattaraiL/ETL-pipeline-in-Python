import os

API_KEY = os.getenv("API_KEY")
API_URL = "http://api.openweathermap.org/data/2.5/forecast?"
LOCATION = {"latitude" : 27.717245,
            "longitude" : 85.323959 }

DB_CONFIG = {
    "host": "localhost",
    "port": 5432, 
    "dbname": "weather_db",
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}