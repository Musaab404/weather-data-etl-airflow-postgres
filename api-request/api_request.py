import requests
import json




api_key = "d399529f1360debbcc1041658645e76b"
api_url = f"http://api.weatherstack.com/forecast?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching data from API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        print("api request successful!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        raise




def dummy_fetch_data():
    return  {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-05-28 11:45', 'localtime_epoch': 1779968700, 'utc_offset': '-4.0'}, 'current': {'observation_time': '03:45 PM', 'temperature': 22, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'air_quality': {'co': '134.85', 'no2': '4.05', 'o3': '78', 'so2': '1.25', 'pm2_5': '3.35', 'pm10': '3.45', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 19, 'wind_degree': 347, 'wind_dir': 'NNW', 'pressure': 1012, 'precip': 0, 'humidity': 48, 'cloudcover': 25, 'feelslike': 24, 'uv_index': 6, 'visibility': 16, 'is_day': 'yes'}, 'forecast': {'2026-05-27': {'date': '2026-05-27', 'date_epoch': 1779840000, 'astro': {'sunrise': '05:30 AM', 'sunset': '08:17 PM', 'moonrise': '05:05 PM', 'moonset': '03:07 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 83}, 'mintemp': 18, 'maxtemp': 32, 'avgtemp': 25, 'totalsnow': 0, 'sunhour': 14.8, 'uv_index': 4, 'air_quality': {'co': '259.9300000000001', 'no2': '33.534000000000006', 'o3': '67.56', 'so2': '3.313999999999999', 'pm2_5': '18.465999999999998', 'pm10': '18.906', 'us-epa-index': '2', 'gb-defra-index': '2'}}}}



