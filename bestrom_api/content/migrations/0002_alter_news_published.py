# Generated by Django 3.2.8 on 2023-10-31 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 8, 12, 10, 523447), verbose_name='Время публикации'),
        ),
    ]