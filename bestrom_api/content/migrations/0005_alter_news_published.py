# Generated by Django 3.2.8 on 2024-11-25 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_news_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 25, 7, 54, 33, 404547), verbose_name='Время публикации'),
        ),
    ]
