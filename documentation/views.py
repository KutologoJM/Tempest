from django.shortcuts import render
import markdown
from django.conf import settings


def render_md_docs(request, doc_path):
    project_root = settings.PROJECT_ROOT
    doc_path = open(f"{project_root}/documentation/templates/docs/{doc_path}.md").read() # TODO check if vulnerable to path traversal
    html = markdown.markdown(doc_path, extensions=["fenced_code", "tables"])
    return render(request, "rendered_md.html", {"html": html})
