from django.views.generic import ListView, DetailView
from documentation import models


class ModelsDocumentationDetailView(DetailView):
    queryset = models.ModelVariable.objects.all()
    template_name = "docs/documentation_detail.html"
    context_object_name = "model_doc"
    slug_field = "name_of_parent_model"
    slug_url_kwarg = "name_of_parent_model"


class ModelsDocumentationListView(ListView):
    template_name = "docs/models_documentation.html"
    context_object_name = "model_doc"

    def get_queryset(self):
        return models.ModelVariable.objects.filter(
            name_of_parent_model=self.kwargs['name_of_parent_model']
        )
