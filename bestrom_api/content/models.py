import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Page(models.Model):
    title = models.CharField(verbose_name='Title страницы', max_length=256, null=True)
    title_en = models.CharField(verbose_name='Перевод title', max_length=256, null=True)
    description = models.CharField(verbose_name='Description страницы', max_length=512, null=True, blank=True)
    description_en = models.CharField(verbose_name='Перевод Description страницы', max_length=512, null=True, blank=True)
    keywords = models.CharField(verbose_name='Keywords страницы', max_length=256, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'


class Block(models.Model):
    name = models.CharField(verbose_name='Наименование блока', max_length=256, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='blocks')

    def __str__(self):
        return str(self.page.title) + ' ' + str(self.name)

    class Meta:
        verbose_name_plural = 'Блоки'
        verbose_name = 'Блок'


class ContFile(models.Model):
    alt = models.CharField(verbose_name='тэг Alt', max_length=100, null=True)
    file = models.FileField(verbose_name='Файл', upload_to='content/files', blank=True)

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name_plural = 'Файлы'
        verbose_name = 'Файл'


class Content(models.Model):
    name = models.CharField(verbose_name='Название', max_length=1024, null=True)
    name_en = models.CharField(verbose_name='Перевод наименования', max_length=1024, null=True, blank=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='contents')
    file = models.ManyToManyField(ContFile, verbose_name='Изображение', blank=True)
    text = models.TextField(verbose_name='Содержимое', null=True, blank=True)
    text_en = models.TextField(verbose_name='Перевод', null=True, blank=True)

    def __str__(self):
        return str(self.block.page.title) + ' ' + str(self.block.name) + ' ' + str(self.name)

    class Meta:
        verbose_name_plural = 'Контент'
        verbose_name = 'Контент'


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование партнера', null=True)
    logo = models.ImageField(upload_to='content/files/partner', verbose_name='Логотип', null=True, blank=True)
    description = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)
    description_en = RichTextUploadingField(verbose_name='Перевод', null=True, blank=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнер'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование клиента', null=True)
    logo = models.ImageField(upload_to='content/files/clients', verbose_name='Логотип', null=True, blank=True)
    description = RichTextUploadingField(verbose_name='Описание', null=True, blank=True)
    description_en = RichTextUploadingField(verbose_name='Перевод', null=True, blank=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'


class News(models.Model):
    name = models.CharField(max_length=256, verbose_name='Заголовок новости', null=True)
    name_en = models.CharField(max_length=256, verbose_name='Перевод заголовка', null=True)
    img = models.ImageField(upload_to='content/files/partner', verbose_name='Изображение', null=True, blank=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, unique=True)
    mini_description = RichTextUploadingField(verbose_name='Краткое содержание', null=True, blank=True)
    mini_description_en = RichTextUploadingField(verbose_name='Перевод содержания', null=True, blank=True)
    description = RichTextUploadingField(verbose_name='Текст', null=True, blank=True)
    description_en = RichTextUploadingField(verbose_name='Перевод текста', null=True, blank=True)
    published = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Время публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'


class Vacancy(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование вакансии', null=True)
    img = models.ImageField(upload_to='content/files/vacancy', verbose_name='Изображение', null=True, blank=True)
    alt = models.CharField(max_length=100, verbose_name='Тэг alt', null=True, unique=True)
    requirements = RichTextUploadingField(verbose_name='Требования', blank=True, null=True)
    skills = RichTextUploadingField(verbose_name='Навыки', blank=True, null=True)
    salary = models.CharField(max_length=100, verbose_name='Зарплата', blank=True, null=True)
    education = models.CharField(max_length=100, verbose_name='Образование', blank=True, null=True)
    experience = models.CharField(max_length=100, verbose_name='Опыт работы', blank=True, null=True)
    youget = RichTextUploadingField(verbose_name='Вы получаете', blank=True, null=True)
    rus_ver = models.BooleanField(verbose_name='Русская версия', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'


class History(models.Model):
    year = models.IntegerField(verbose_name='Год', default=1900)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    description_en = models.TextField(verbose_name='Перевод', null=True, blank=True)
    img = models.FileField(verbose_name='Изображение', null=True, blank=True, upload_to='content/files/history')

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name_plural = 'Карусель годов'
        verbose_name = 'Год'
