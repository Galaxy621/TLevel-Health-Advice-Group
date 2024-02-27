import requests

class WeatherAPI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WeatherAPI, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        ...

    def get_location_info(location: str) -> dict | None: 
        endpoint = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
        response = requests.get(endpoint)

        if response.status_code != 200: return None
        
        items = response.json().get("results", None)
        if not items: return None
        if len(items) <= 0: return None

        return items[0]
    
    def get_weather_info(lat: float, long: float) -> dict | None:
        endpoint = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}"