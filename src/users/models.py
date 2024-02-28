from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='users', blank=True, null=True, verbose_name='Фото')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    phone_number = PhoneNumberField(region="UA", blank=True, null=True, verbose_name='Номер телефону')

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
