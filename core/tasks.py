from __future__ import absolute_import, unicode_literals
from assessment.celery import app
from django.core.mail import send_mail
from core.models import User  # Adjust this import based on your actual User model


@app.task
def send_email_task(email, message, **kwargs):
    try:
        print(email, message)
        # Placeholder for email sending logic
        send_mail(
            'welcome to our site',
            message,
            'from@example.com',  # Adjust the sender email
            [email],
            fail_silently=False,
        )
        return f"Email sent to {email}"
    except User.DoesNotExist:
        return 'User not found'

