# Generated by Django 3.2.8 on 2025-03-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20241125_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryfilters',
            name='slug',
            field=models.SlugField(max_length=256, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='filters',
            name='slug',
            field=models.SlugField(max_length=256, null=True, unique=True, verbose_name='URL'),
        ),
    ]
