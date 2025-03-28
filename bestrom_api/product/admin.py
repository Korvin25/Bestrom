from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from . import models


# Register your models here.
class SliderInstanceInline(admin.TabularInline):
    model = models.SliderProd
    extra = 0


class PropertyInstanceInline(admin.StackedInline):
    model = models.ProductPropertyValue
    extra = 0


class SolutionInstanceInline(admin.TabularInline):
    model = models.Solution
    extra = 0


class PacketInstanceInline(admin.TabularInline):
    model = models.Product.Packet.through
    extra = 0
    verbose_name = u"Пакет"
    verbose_name_plural = u"Пакеты"

class ItemsInstanceInline(admin.TabularInline):
    model = models.Product.Items.through
    extra = 0
    verbose_name = u"Продукт"
    verbose_name_plural = u"Продукты"


class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('order', 'name', 'slug', 'active') 
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PropertyInstanceInline, SliderInstanceInline, ItemsInstanceInline,
               SolutionInstanceInline, PacketInstanceInline]
    
    
class PacketAdmin(admin.ModelAdmin):
    list_display = ('name', 'essid', 'active') 
    
    
class PacketSeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'essid') 


class CategoryFiltersAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    
    
class FiltersAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Product, ProductAdmin)
#admin.site.register(models.SliderProd)
admin.site.register(models.ProductProperties)
# admin.site.register(models.ProductPropertyValue)
admin.site.register(models.Items)
admin.site.register(models.ItemsExample)
# admin.site.register(models.Equipment)
# admin.site.register(models.Solution)
# admin.site.register(models.Docs)
admin.site.register(models.CategoryFilters, CategoryFiltersAdmin)
admin.site.register(models.Filters, FiltersAdmin)
admin.site.register(models.Packet, PacketAdmin)
admin.site.register(models.PacketOptions)
admin.site.register(models.PacketSeam, PacketSeamAdmin)
