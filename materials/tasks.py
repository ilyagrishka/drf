from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_refresh_email(email, ):
    send_mail("Обновление курсов", "У вас есть обновление по курсам и урокам ", settings.EMAIL_HOST_USER, [email])


def send_email_last_login():
    today = timezone.now().today().date()
    users_to_block = User.objects.filter(last_login=(today() - timedelta(days=30)))
    for user in users_to_block:
        if not user.is_active:
            send_mail("вы заблокированы", "вы заблокированы", EMAIL_HOST_USER)

        user.save()
