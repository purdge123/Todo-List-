from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reminder_email(email_address):
    send_mail(
        'Task Reminder',
        'This is a reminder for your upcoming task.',
        'from@example.com',
        [email_address],
        fail_silently=False,
    )
