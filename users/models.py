from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(upload_to="users/avatars", verbose_name="аватар", blank=True, null=True)
    phone_number = models.CharField(max_length=23, verbose_name="телефон", blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name="страна")

    token = models.CharField(max_length=100, verbose_name="token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    # objects = CustomUserManager()

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи "

        def __str__(self):
            return self.email
