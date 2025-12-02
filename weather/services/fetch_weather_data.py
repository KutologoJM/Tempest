import httpx
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather_data() -> dict:
    """

    :return:
    """
    lat = os.getenv("LAT")
    lon = os.getenv("LON")
    api_key = os.getenv("TEMPEST_WEATHER")
    exclusion = 'minutely'
    endpoint = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclusion}&appid={api_key}&units=metric&lang=en"

    try:
        weather_data = httpx.get(endpoint).json()
    except httpx.ConnectTimeout:
        print("Connection timed out")
        weather_data = None
    return weather_data


def get_current_weather_data() -> dict:
    """

    :return:
    """
    weather_data = get_weather_data()
    current_weather = weather_data["current"]
    nested_weather = weather_data["current"]["weather"][0]
    icon = nested_weather["icon"]
    icon_image_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    weather_data["current"]["weather"][0]["icon"] = icon_image_url

    return current_weather


def get_hourly_weather_data() -> dict:
    """

    :return:
    """
    weather_data = get_weather_data()
    hourly_weather = weather_data["hourly"]
    return hourly_weather


def get_daily_weather_data() -> dict:
    """

    :return:
    """
    weather_data = get_weather_data()
    daily_weather = weather_data["daily"]
    return daily_weather


def test_data() -> dict:
    """
    Fetches the weather data from the API and filters out the current.weather object for testing purposes

    :return:
    """
    weather_data = get_weather_data()
    test_weather = weather_data["current"]["weather"][0]
    icon = test_weather["icon"]
    icon_image_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    test_weather["icon"] = icon_image_url
    return test_weather

if __name__ == "__main__":
    output = get_current_weather_data()
    print(output)
