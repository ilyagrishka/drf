from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone


@shared_task
def send_refresh_email(email, ):
    send_mail("Обновление курсов", "У вас есть обновление по курсам и урокам ", settings.EMAIL_HOST_USER, [email])


def send_email_last_login():
    today = timezone.now().today()
