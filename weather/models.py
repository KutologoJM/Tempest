from datetime import datetime
from django.db import models


# Create your models here.

class CurrentWeatherModel(models.Model):
    dt = models.BigIntegerField(primary_key=True) # unix
    sunrise = models.BigIntegerField() # unix
    sunset = models.BigIntegerField() # unix
    temp = models.FloatField() # degrees
    feels_like = models.FloatField() # degrees
    pressure = models.IntegerField() # hPa
    humidity = models.IntegerField() # percentage
    dewpoint = models.FloatField() # degrees
    uv_index = models.IntegerField()  # uv index
    clouds = models.IntegerField()  # percentage
    visibility = models.IntegerField() # metres/sec
    wind_speed = models.FloatField() # metres/sec
    wind_gust = models.FloatField(blank=True, null=True) # metres/sec
    wind_deg = models.IntegerField() # degrees meteorological
    rain = models.IntegerField(null=True, blank=True) # mm/h
    snow = models.IntegerField(null=True, blank=True) # mm/h
    weather_id = models.IntegerField()
    weather_main = models.CharField(max_length=120) # name of weather event
    weather_description = models.CharField(max_length=200)
    weather_icon = models.URLField() # link to weather event icon

    @property
    def human_readable_datetime(self):
        return datetime.fromtimestamp(self.dt).strftime("%H:%M")

    @property
    def human_readable_sunrise(self):
        return datetime.fromtimestamp(self.sunrise).strftime("%H:%M")

    @property
    def human_readable_sunset(self):
        return datetime.fromtimestamp(self.sunset).strftime("%H:%M")