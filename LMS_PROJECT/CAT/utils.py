import threading
from django.core.mail import send_mail
from .signals import email_sent_signal
from django.dispatch import receiver
import logging

def send_email_async(subject, message, from_email, recipient_list):
    def email_send():
        send_mail(subject, message, from_email, recipient_list)
        email_sent_signal.send(sender=None)

    thread = threading.Thread(target=email_send)
    thread.start()


@receiver(email_sent_signal)
def email_sent_handler(sender, **kwargs):
    # Log the email sending event
    logging.info('Email sent successfully.')
