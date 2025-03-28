from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from content.models import Client

class Product(models.Model):
    active = models.BooleanField('Показать на сайте', default=True)
    name = models.CharField(max_length=100, verbose_name='Наименование товара', null=True)
    slug = models.SlugField(max_length=256, verbose_name='URL', null=True, unique=True)
    name_en = models.CharField(max_length=100, verbose_name='Перевод(Наименование товара)', null=True)
    description = RichTextUploadingField(verbose_name='Описание товара', null=True, blank=True)
    description_en = RichTextUploadingField(verbose_name='Перевод(Описание товара)', null=True, blank=True)
    clients = models.ManyToManyField(Client, related_name='Product', verbose_name='Клиенты купившие товар', null=True, blank=True)
    category_filters = models.ManyToManyField('Filters', verbose_name='Фильтры(Категории)', related_name='Product', null=True, blank=True)
    equipments = models.ManyToManyField('Product', related_name='Equipment', verbose_name='Доп оборудование', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    seo_title = models.CharField('Тайтл SEO', max_length=300, blank=True)
    seo_description = models.CharField('Описание SEO', max_length=300, blank=True)
    seo_title_en = models.CharField('Перевод(Тайтл SEO)', max_length=300, blank=True)
    seo_description_en = models.CharField('Перевод(Описание SEO)', max_length=300, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['order']


class SliderProd(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='SliderProd', verbose_name='Товар')
    img = models.ImageField(verbose_name='Изображение', upload_to='product/files/slider', null=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True)

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name_plural = 'Слайдеры товаров'
        verbose_name = 'Слайдер товара'


class ProductProperties(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование характеристики')
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
    product = models.ManyToManyField(Product, verbose_name='Товар', related_name='ProductProperties',
                                     through='ProductPropertyValue')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Характеристики'
        verbose_name = 'Характеристика'


class ProductPropertyValue(models.Model):
    product = models.ForeignKey(Product, related_name='ProductPropertyValue', on_delete=models.CASCADE)
    product_property = models.ForeignKey(ProductProperties, related_name='PropertyValue', verbose_name='Харакартеристика', on_delete=models.CASCADE)
    name = RichTextUploadingField(verbose_name='Значение характеристики', null=True)
    name_en = RichTextUploadingField(verbose_name='Перевод', null=True)

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
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
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
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
    items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='ItemsExample',
                              verbose_name='Примеры продуктов')
    img = models.ImageField(upload_to='product/files/items_example', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Примеры продуктов'
        verbose_name = 'Пример продукта'


class Solution(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование решения')
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
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
    slug = models.SlugField(max_length=256, verbose_name='URL', null=True, unique=True)
    sort = models.IntegerField(verbose_name='Сортировка', null=True, blank=True)
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
    img = models.ImageField(verbose_name='Изображение', upload_to='product/files/filters', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории фильтров'
        verbose_name = 'Категория фильтра'


class Filters(models.Model):
    cat = models.ForeignKey(CategoryFilters, verbose_name='Категория', on_delete=models.CASCADE, related_name='Filters')
    img = models.ImageField(verbose_name='Изображение', upload_to='product/files/filter', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Наименование фильтра', null=True)
    slug = models.SlugField(max_length=256, verbose_name='URL', null=True, unique=True)
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
    search = models.CharField(max_length=100, verbose_name='Поисковый запрос', null=True)
    seo_title = models.CharField('Тайтл SEO', max_length=300, blank=True)
    seo_description = models.CharField('Описание SEO', max_length=300, blank=True)
    seo_title_en = models.CharField('Перевод(Тайтл SEO)', max_length=300, blank=True)
    seo_description_en = models.CharField('Перевод(Описание SEO)', max_length=300, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фильтры(Категории)'
        verbose_name = 'Фильтр(Категория)'


class Packet(models.Model):
    active = models.BooleanField('Отображать в раскрое', default=True)
    name = models.CharField(max_length=100, verbose_name='Наименование пакета')
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
    product = models.ManyToManyField(Product, related_name='Packet', verbose_name='Товар')
    img = models.ImageField(upload_to='product/files/packet', verbose_name='Изображение')
    drawing = models.ImageField(upload_to='product/files/packet/drawing', verbose_name='Чертеж')
    essid = models.CharField(max_length=10, verbose_name='Идентификатор', blank=True, null=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Пакеты'
        verbose_name = 'Пакет'

class PacketOptions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Опции пакета')
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
    packet = models.ManyToManyField(Packet, related_name='Options', verbose_name='Товар')
    product = models.ManyToManyField(Product, related_name='PacketsOptions', verbose_name='Продукт') 
    img = models.ImageField(upload_to='product/files/packet/options', verbose_name='Изображение')
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Опции пакетов'
        verbose_name = 'Опция пакета'


class PacketSeam(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип шва')
    name_en = models.CharField(max_length=100, verbose_name='Перевод', null=True)
    packet = models.ManyToManyField(Packet, related_name='Seam', verbose_name='Товар')
    img = models.ImageField(upload_to='product/files/packet/seam', verbose_name='Изображение')
    essid = models.CharField(max_length=2, verbose_name='Идентификатор', blank=True, null=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типы швов'
        verbose_name = 'Тип шва'
