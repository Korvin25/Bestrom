# Generated by Django 3.2.8 on 2024-07-20 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20231123_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 20, 13, 31, 4, 655605), verbose_name='Время публикации'),
        ),
    ]
