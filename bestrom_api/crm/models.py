import datetime

from config import settings
from django.core.mail import EmailMessage
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Crm_forms(models.Model):
    dateapp = models.DateTimeField(auto_now=True, verbose_name='Дата поступления')
    type = models.CharField(verbose_name='Тип заявки', max_length=100, null=True, blank=True)
    telephone = models.CharField(verbose_name='Номер телефона', max_length=20, null=True, blank=True)
    email = models.CharField(verbose_name='Почта', max_length=50, null=True, blank=True)
    name = models.CharField(verbose_name='Обращение', max_length=50, null=True, blank=True)
    other = models.TextField(verbose_name='Примечание', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', null=True, blank=True, upload_to='crm/')

    def __str__(self):
        return str(self.dateapp)

    class Meta:
        verbose_name_plural = 'Заявки-обращения'
        verbose_name = 'Заявка-обращение'


@receiver(post_save, sender=Crm_forms)
def add_form(sender, instance, created, **kwargs):
    if created:
        email = EmailMessage(
            'Заявка ' + str(instance.type) + ' ' + str(datetime.datetime.now()),
            body=str(instance.name) + ' ' + str(instance.telephone) + ' ' + str(instance.email) + ' ' + str(
                instance.other),
            from_email=settings.EMAIL_HOST_USER,
            to=settings.EMAIL_ADMINS,
        )
        if instance.file:
            email.attach_file(instance.file.path)
        email.send()
