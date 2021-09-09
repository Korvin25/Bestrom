from django.db import models


# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Title страницы', max_length=256, null=True)
    description = models.CharField(verbose_name='Description страницы', max_length=512, null=True, blank=True)
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
        return self.name

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
    block = models.ForeignKey(Block, on_delete=models.CASCADE,related_name='contents')
    file = models.ManyToManyField(ContFile, blank=True)
    text = models.CharField(verbose_name='Содержимое', max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Контент'
        verbose_name = 'Контент'

