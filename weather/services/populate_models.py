import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tempest.settings.dev")

django.setup()

from fetch_weather_data import get_current_weather_data
from weather.models import CurrentWeatherModel

current_weather = get_current_weather_data()
weather = current_weather["weather"][0]

lookup = {"dt": current_weather["dt"]}

filtered_data = current_weather

defaults = {
    "dt": current_weather["dt"],
    "sunrise": current_weather["sunrise"],
    "sunset": current_weather["sunset"],
    "temp": current_weather["temp"],
    "feels_like": current_weather["feels_like"],
    "pressure": current_weather["pressure"],
    "humidity": current_weather["humidity"],
    "dewpoint": current_weather["dew_point"],
    "uv_index": current_weather["uvi"],
    "clouds": current_weather["clouds"],
    "visibility": current_weather["visibility"],
    "wind_speed": current_weather["wind_speed"],
    "wind_gust": current_weather["wind_gust"],
    "wind_deg": current_weather["wind_deg"],
    "rain": current_weather["rain"],
    "snow": current_weather["snow"],
    "weather_id": weather["id"],
    "weather_main": weather["main"],
    "weather_description": weather["description"],
    "weather_icon": weather["icon"],
}

obj, created = CurrentWeatherModel.objects.update_or_create(defaults=defaults, **lookup)

if created:
    print("Created model")
else:
    print("Failed to create model")
