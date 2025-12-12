from django.db import models
from django.utils.text import slugify


class ModelField(models.Model):
    field_name = models.CharField(max_length=100)
    field_description = models.TextField()

    def __str__(self):
        return self.field_name


class FieldArgument(models.Model):
    argument_name = models.CharField(max_length=100)
    argument_description = models.TextField()

    def __str__(self):
        return self.argument_name


class ModelVariable(models.Model):
    model = models.ForeignKey("ModelDocEntry", on_delete=models.CASCADE)
    variable_name = models.CharField(max_length=100)
    variable_description = models.TextField()
    variable_is_required = models.BooleanField(default=False)
    model_field = models.ForeignKey("ModelField",
                                    on_delete=models.CASCADE)
    field_arguments = models.ManyToManyField("FieldArgument",
                                             through="FieldArgumentPair", related_name="model_variables")
    name_of_parent_model = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.name_of_parent_model:
            self.name_of_parent_model = slugify(self.model.model_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.model.model_name}: {self.variable_name}"

    class Meta:
        unique_together = (("model", "variable_name"),)


class FieldArgumentPair(models.Model):
    variable_name = models.ForeignKey(ModelVariable,
                                      on_delete=models.CASCADE, related_name="argument_pairs")  # holds the associated field arguments m2m field
    field_argument = models.ForeignKey("FieldArgument", on_delete=models.CASCADE)
    argument_value = models.CharField(max_length=100)
    argument_value_description = models.TextField(default="argument_description")

    def __str__(self):
        return f"{self.variable_name}: {self.field_argument} = {self.argument_value}"


class ModelDocEntry(models.Model):  # recipe
    parent_project = models.CharField(max_length=100, help_text="The name of the django project this item belongs to.")
    parent_app = models.CharField(max_length=100, help_text="The name of the django app this item belongs to.")
    module_type = models.CharField(max_length=100, default="model",
                                   help_text="The type of the module(model, view, url) this item belongs to.")
    model_name = models.CharField(max_length=100, help_text="The name of the model being documented.")
    model_description = models.TextField()

    def __str__(self):
        return f"{self.parent_project} {self.model_name}"
