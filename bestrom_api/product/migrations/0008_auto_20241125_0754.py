# Generated by Django 3.2.8 on 2024-11-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_filters_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='packet',
            name='essid',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Идентификатор'),
        ),
        migrations.AddField(
            model_name='packetseam',
            name='essid',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Идентификатор'),
        ),
    ]
