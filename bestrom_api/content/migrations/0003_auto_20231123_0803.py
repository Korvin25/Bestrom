# Generated by Django 3.2.8 on 2023-11-23 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_news_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]