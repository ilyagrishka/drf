from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(upload_to="users/avatars", verbose_name="аватар", blank=True, null=True)
    phone_number = models.CharField(max_length=23, verbose_name="телефон", blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name="страна")
    last_login = models.DateTimeField(max_length=50, verbose_name="дата последнего захода")

    token = models.CharField(max_length=100, verbose_name="token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи "

        def __str__(self):
            return self.email


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="пользователь", blank=True, null=True, )
    payments_day = models.DateTimeField(verbose_name="дата оплаты")
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="оплаченный курс", blank=True,
                                    null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name="оплаченный урок", blank=True,
                                    null=True)
    sum_of_payments = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_method = models.CharField(verbose_name="способ оплаты")
    session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="id сессии",
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="ссылка на оплату",
    )

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплата"

    def __str__(self):
        return self.sum_of_payments
