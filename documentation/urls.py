from . import views
from django.urls import path

urlpatterns = [
    path('<path:doc_path>/', views.render_md_docs, name='doc_render'),
]
