from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

def send_verification_email(user):
    # Retrieve the user's email verification token.
    token = user.email_verification_token
    # Construct the verification URL using the frontend base URL.
    verification_link = f"{settings.FRONTEND_URL}/#/email-verification?token={token}"
    subject = 'E-Mail Verifizierung'
    message = f'Bitte klicken Sie auf den folgenden Link, um Ihre E-Mail zu verifizieren: {verification_link}'
    # Send the verification email.
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    
def send_password_reset_email(user):
    # Build the password reset URL using the user's reset token.
    reset_link = f"{settings.FRONTEND_URL}/#/password-reset?token={user.password_reset_token}"
    subject = 'Passwort zurücksetzen'
    message = f'Bitte klicken Sie auf den folgenden Link, um Ihr Passwort zurückzusetzen: {reset_link}'
    # Send the password reset email.
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
