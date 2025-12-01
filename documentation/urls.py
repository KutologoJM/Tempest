from . import views
from django.urls import path

from .views import AppDocView

urlpatterns = [
    path("", AppDocView.as_view(), name="app_documentation"),
]
