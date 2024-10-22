from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
import logging

from user.models import PasswordReset


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    request = kwargs.get('request')
    ip_address = request.META.get('REMOTE_ADDR') if request else None
    
    # send an e-mail to the user
    reset_password_url = "http://videoflix.juridev.de/forgot-password-reset?token={}".format(reset_password_token.key)
    
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': reset_password_url
    }

    # render email text
    email_html_message = render_to_string('email/password_reset_email.html', context)
    email_plaintext_message = render_to_string('email/password_reset_email.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Videoflix"),
        # message:
        email_plaintext_message,
        # from:
        "info.videoflix@juridev.de",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
    
    if ip_address:
        try:
            PasswordReset.objects.create(
                email=reset_password_token.user.email,
                token=reset_password_token.key,
                ip_address=ip_address
            )
        except Exception as e:
            logging.loggers.error(f"Error saving password reset with IP {ip_address}: {e}")