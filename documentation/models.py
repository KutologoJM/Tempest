from django.db import models
from martor.models import MartorField

class AppDoc(models.Model):
    title = models.CharField(max_length=200)
    content = MartorField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
