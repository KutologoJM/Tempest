from django.views.generic import TemplateView, DetailView
from .models import CurrentWeatherModel

# Create your views here.

class CurrentWeatherView(DetailView):
    model = CurrentWeatherModel
    template_name = "current/current_weather.html"
    context_object_name = "current"
    queryset = CurrentWeatherModel.objects.all()
    lookup_field = 'dt'
    slug = 'dt'

class DailyWeatherView(TemplateView):
    template_name = "daily_weather.html"


class HourlyWeatherView(TemplateView):
    template_name = "hourly_weather.html"
