from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.CharField(max_length=25,
                             unique=True,
                             verbose_name="Email",
                             help_text="Введите email. Он будет"
                                       " использован для авторизации.")
    avatar = models.ImageField(upload_to="users/avatars/",
                               verbose_name="Фото профиля",
                               blank=True,
                               null=True)
    phone_number = models.CharField(max_length=15,
                                    verbose_name="Телефон",
                                    help_text="Введите номер телефона",
                                    blank=True,
                                    null=True)
    country = models.CharField(max_length=50,
                               verbose_name="Страна",
                               help_text="Введите страну проживания",
                               blank=True,
                               null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
