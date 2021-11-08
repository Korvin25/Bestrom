from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Content)
admin.site.register(models.Page)
admin.site.register(models.Block)
admin.site.register(models.ContFile)
admin.site.register(models.Partner)
admin.site.register(models.Client)
admin.site.register(models.News)
admin.site.register(models.Vacancy)
admin.site.register(models.History)