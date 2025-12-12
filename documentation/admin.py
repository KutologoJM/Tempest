from django.contrib import admin
from . import models

admin.site.register(models.ModelVariable)
admin.site.register(models.FieldArgument)
admin.site.register(models.ModelField)
admin.site.register(models.FieldArgumentPair)
admin.site.register(models.ModelDocEntry)
