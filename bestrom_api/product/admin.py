from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.SliderProd)
admin.site.register(models.ProductProperties)
admin.site.register(models.ProductPropertyValue)
admin.site.register(models.Items)
admin.site.register(models.ItemsExample)
admin.site.register(models.Equipment)
admin.site.register(models.Solution)
admin.site.register(models.Docs)