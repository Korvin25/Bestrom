from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

from . import models


class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        # for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list


class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'block', 'active')
    list_filter = ('block',)


admin.site = MyAdminSite()
# Register your models here.
admin.site.register(models.Page)
admin.site.register(models.Block)
admin.site.register(models.Content, ContentAdmin)
admin.site.register(models.News)
admin.site.register(models.Partner)
admin.site.register(models.Client)
admin.site.register(models.Vacancy)
admin.site.register(models.History)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
