from . import views
from django.urls import path

urlpatterns = [
    path("models/<slug:name_of_parent_model>/", views.ModelsDocumentationListView.as_view(), name="models=-documentation"),
]
