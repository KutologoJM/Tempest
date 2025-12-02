from django.views.generic import ListView

from .models import AppDoc


class AppDocView(ListView):
    template_name = "app_documentation/test_app.html"
    model = AppDoc
    context_object_name = "app_docs"
    queryset = AppDoc.objects.all()
