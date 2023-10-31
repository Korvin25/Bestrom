# Generated by Django 3.2.8 on 2023-10-30 08:37

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verbose_name', models.CharField(max_length=256, null=True, verbose_name='Наименование для панели админа')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='Наименование блока')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоки',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Наименование клиента')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='content/files/clients', verbose_name='Логотип')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Перевод')),
                ('alt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тэг alt')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='ContFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=100, null=True, verbose_name='тэг Alt')),
                ('file', models.FileField(blank=True, upload_to='content/files', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=1900, verbose_name='Год')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Перевод')),
                ('img', models.FileField(blank=True, null=True, upload_to='content/files/history', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Год',
                'verbose_name_plural': 'Карусель годов',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='Заголовок новости')),
                ('name_en', models.CharField(max_length=256, null=True, verbose_name='Перевод заголовка')),
                ('img', models.ImageField(blank=True, null=True, upload_to='content/files/partner', verbose_name='Изображение')),
                ('alt', models.CharField(max_length=100, null=True, unique=True, verbose_name='Тэг alt')),
                ('mini_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Краткое содержание')),
                ('mini_description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Перевод содержания')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Перевод текста')),
                ('published', models.DateTimeField(default=datetime.datetime(2023, 10, 30, 8, 37, 28, 197354), verbose_name='Время публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verbose_name', models.CharField(max_length=256, null=True, verbose_name='Наименование для панели админа')),
                ('title', models.CharField(max_length=256, null=True, verbose_name='Title страницы')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='Перевод title')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='Description страницы')),
                ('description_en', models.CharField(blank=True, max_length=512, null=True, verbose_name='Перевод Description страницы')),
                ('keywords', models.CharField(blank=True, max_length=256, null=True, verbose_name='Keywords страницы')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Наименование партнера')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='content/files/partner', verbose_name='Логотип')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Перевод')),
                ('alt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тэг alt')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='Наименование вакансии')),
                ('img', models.ImageField(blank=True, null=True, upload_to='content/files/vacancy', verbose_name='Изображение')),
                ('alt', models.CharField(max_length=100, null=True, unique=True, verbose_name='Тэг alt')),
                ('requirements', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Требования')),
                ('skills', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Навыки')),
                ('salary', models.CharField(blank=True, max_length=100, null=True, verbose_name='Зарплата')),
                ('education', models.CharField(blank=True, max_length=100, null=True, verbose_name='Образование')),
                ('experience', models.CharField(blank=True, max_length=100, null=True, verbose_name='Опыт работы')),
                ('youget', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Вы получаете')),
                ('rus_ver', models.BooleanField(default=True, verbose_name='Русская версия')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True, verbose_name='Название')),
                ('name_en', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Перевод наименования')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('text_en', models.TextField(blank=True, null=True, verbose_name='Перевод')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='content.block', verbose_name='Блок')),
                ('file', models.ManyToManyField(blank=True, to='content.ContFile', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='content.page'),
        ),
    ]