from django.db import models


class ModelFieldTypesModel(models.Model):
    field_type_name = models.CharField(max_length=100)
    field_type_description = models.TextField()

    def __str__(self):
        return self.field_type_name


class ModelFieldArgumentModel(models.Model):
    argument_name = models.CharField(max_length=100)
    argument_description = models.TextField()

    def __str__(self):
        return self.argument_name


class ModelFieldsModel(models.Model):  # recipe sources
    model_field_name = models.CharField(max_length=100, unique=True)
    model_field_description = models.TextField()
    model_field_is_required = models.BooleanField(default=False)
    model_field_type = models.ForeignKey("ModelFieldTypesModel",
                                         on_delete=models.CASCADE)
    model_field_arguments = models.ManyToManyField("ModelFieldArgumentModel",
                                                   through="FieldArgumentMapping")

    def __str__(self):
        return self.model_field_name


class FieldArgumentMapping(models.Model):
    model_field = models.ForeignKey(ModelFieldsModel, on_delete=models.CASCADE)
    field_argument = models.ForeignKey("ModelFieldArgumentModel", on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    value_description = models.TextField()

    def __str__(self):
        return f"{self.model_field}: {self.field_argument} = {self.value}"


class ModelsDocumentationModel(models.Model):  # recipe
    parent_project = models.CharField(max_length=100, help_text="The name of the django project this item belongs to.")
    parent_app = models.CharField(max_length=100, help_text="The name of the django app this item belongs to.")
    module_type = models.CharField(max_length=100, default="model",
                                   help_text="The type of the module(model, view, url) this item belongs to.")
    model_name = models.CharField(max_length=100, help_text="The name of the model being documented.")
    model_description = models.TextField()
    model_fields = models.ManyToManyField("ModelFieldsModel", related_name="fields",
                                          help_text="The fields (CharField, ForeignKey) this model has.")

    def __str__(self):
        return f"{self.parent_project} {self.model_name}"
