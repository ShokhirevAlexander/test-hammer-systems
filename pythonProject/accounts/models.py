import random

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .utils import invite_generator
from accounts.managers import UserManager


class CustomeUser(AbstractBaseUser, PermissionsMixin):
    """ Модель пользователя """

    phone_regex = RegexValidator(
        regex=r'^[8]\d{10}$',
        message='Введите допустимое значение')
    phone_number = models.CharField(verbose_name='номер телефона',
                                    validators=[phone_regex],
                                    max_length=11, unique=True)
    invite_code = models.CharField(
        max_length=6, default=invite_generator,
        unique=True, verbose_name='инвайт код'
    )
    password_phone = models.CharField(max_length=4,
                                      verbose_name='одноразовый пароль',
                                      null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.password_phone = random.randint(1000, 9999)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
