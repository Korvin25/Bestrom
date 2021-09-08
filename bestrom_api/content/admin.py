from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Content)
admin.site.register(models.Page)
admin.site.register(models.Block)
admin.site.register(models.ContFile)