from django.db import models
from content.models import Client


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование товара', null=True)
    description = models.CharField(max_length=100, verbose_name='Описание товара', null=True, blank=True)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты купившие товар', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'


class SliderProd(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='SliderProd', verbose_name='Товар')
    img = models.ImageField(verbose_name='Изображение', upload_to='product/files/slider', null=True, blank=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name_plural = 'Слайдеры товаров'
        verbose_name = 'Слайдер товара'


class ProductProperties(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование характеристики')
    product = models.ManyToManyField(Product, verbose_name='Товар', related_name='ProductProperties',
                                     through='ProductPropertyValue')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Характеристики'
        verbose_name = 'Характеристика'


class ProductPropertyValue(models.Model):
    product = models.ForeignKey(Product, related_name='ProductPropertyValue', on_delete=models.CASCADE)
    product_property = models.ForeignKey(ProductProperties, related_name='PropertyValue', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Значение характеристики', null=True)

    def __str__(self):
        return str(self.product.name) + ' ' + str(self.product_property.name)

    class Meta:
        verbose_name_plural = 'Значения характеристик'
        verbose_name = 'Значение характеристики'


class Docs(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование документа')
    product = models.ForeignKey(Product, related_name='Docs', on_delete=models.CASCADE, verbose_name='Товар')
    file = models.FileField(verbose_name='Документация', upload_to='product/files/docs', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Документы'
        verbose_name = 'Документ'


class Items(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта для работы')
    product = models.ManyToManyField(Product, related_name='Items', blank=True)
    img = models.ImageField(upload_to='product/files/items', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Продукты для работы'
        verbose_name = 'Продукт'


class ItemsExample(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование примера продукта')
    items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='ItemsExample',
                              verbose_name='Примеры продуктов')
    img = models.ImageField(upload_to='product/files/items_example', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Примеры продуктов'
        verbose_name = 'Пример продукта'


class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование оборудования')
    product = models.ManyToManyField(Product, related_name='Equipment', verbose_name='Товар')
    img = models.ImageField(upload_to='product/files/equipment', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Дополнительное оборудование'
        verbose_name = 'Дополнительное оборудование'


class Solution(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование решения')
    product = models.ForeignKey(Product, related_name='Solution', on_delete=models.CASCADE, verbose_name='Товар')
    img = models.ImageField(upload_to='product/files/solution', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Готовые решения'
        verbose_name = 'Готовое решение'


class CategoryFilters(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    img = models.ImageField(verbose_name='Изображение', upload_to='product/files/filters', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории фильтров'
        verbose_name = 'Категория фильтра'


class Filters(models.Model):
    cat = models.ForeignKey(CategoryFilters, verbose_name='Категория', on_delete=models.CASCADE, related_name='Filters')
    name = models.CharField(max_length=100, verbose_name='Наименование фильтра', null=True)
    search = models.CharField(max_length=100, verbose_name='Поисковый запрос', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фильтры'
        verbose_name = 'Фильтр'


class Packet(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование пакета')
    product = models.ManyToManyField(Product, related_name='Packet', on_delete=models.CASCADE, verbose_name='Товар')
    img = models.ImageField(upload_to='product/files/packet', verbose_name='Изображение')
    drawing = models.ImageField(upload_to='product/files/packet/drawing', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Пакеты'
        verbose_name = 'Пакет'

class PacketOptions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Опции пакета')
    packet = models.ManyToManyField(Packet, related_name='Options', on_delete=models.CASCADE, verbose_name='Товар')
    img = models.ImageField(upload_to='product/files/packet/options', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Опции пакетов'
        verbose_name = 'Опция пакета'


class PacketSeam(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип шва')
    packet = models.ManyToManyField(Packet, related_name='Seam', on_delete=models.CASCADE, verbose_name='Товар')
    img = models.ImageField(upload_to='product/files/packet/seam', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типы швов'
        verbose_name = 'Тип шва'
