import datetime

from django.db import models
from django.core.mail import send_mail
from config import settings

# Create your models here.
class Crm_forms(models.Model):
    dateapp = models.DateTimeField(auto_now=True, verbose_name='Дата поступления')
    type = models.CharField(verbose_name='Тип заявки', max_length=100, null=True, blank=True)
    telephone = models.CharField(verbose_name='Номер телефона', max_length=20, null=True, blank=True)
    email = models.CharField(verbose_name='Почта', max_length=50, null=True, blank=True)
    name = models.CharField(verbose_name='Обращение', max_length=50, null=True, blank=True)
    other = models.TextField(verbose_name='Примечание',null=True, blank=True)
    file = models.FileField(verbose_name='Файл', null=True, blank=True, upload_to='crm/')

    def __str__(self):
        return str(self.dateapp)

    def save(self, *args, **kwargs):

        send_mail('Заявка '+str(self.type)+' '+str(datetime.datetime.now()), str(self.name)+' '+str(self.telephone)+' '+str(self.email)+' '+str(self.other), settings.EMAIL_HOST_USER,
                  ['ivan@adving.ru','bexram33@mail.ru'], fail_silently=False)
        super().save(*args, **kwargs)