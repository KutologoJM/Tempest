from django.urls import path
from weather.views import CurrentWeatherView, DailyWeatherView, HourlyWeatherView

urlpatterns = [
    path('current-forecast/<int:dt>/', CurrentWeatherView.as_view(), name='current-weather-forecast'),
    path('daily-forecast/', DailyWeatherView.as_view(), name='daily-weather-forecast'),
    path('hourly-forecast/', HourlyWeatherView.as_view(), name='hourly-weather-forecast'),
]
