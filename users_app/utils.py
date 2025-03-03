# from django.core.mail import send_mail
# from django.urls import reverse
# from django.conf import settings

# def send_verification_email(user):
#     token = user.email_verification_token
#     verification_link = f"{settings.FRONTEND_URL}/#/email-verification?token={token}"
#     subject = 'E-Mail Verifizierung'
#     message = f'Bitte klicken Sie auf den folgenden Link, um Ihre E-Mail zu verifizieren: {verification_link}'
#     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    
# def send_password_reset_email(user):
#     reset_link = f"{settings.FRONTEND_URL}/#/password-reset?token={user.password_reset_token}"
#     subject = 'Passwort zurücksetzen'
#     message = f'Bitte klicken Sie auf den folgenden Link, um Ihr Passwort zurückzusetzen: {reset_link}'
#     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.conf import settings

# def send_verification_email(user):
#     verification_link = f"{settings.FRONTEND_URL}/#/email-verification?token={user.email_verification_token}"
#     subject = 'E-Mail Verifizierung'
#     context = {
#         'user': user,
#         'verification_link': verification_link,
#         'current_year': 2025,  # Alternativ dynamisch ermitteln
#     }
#     html_message = render_to_string('emails/verification_email.html', context)
#     send_mail(subject, "", settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)

# def send_password_reset_email(user):
#     reset_link = f"{settings.FRONTEND_URL}/#/password-reset?token={user.password_reset_token}"
#     subject = 'Passwort zurücksetzen'
#     context = {
#         'user': user,
#         'reset_link': reset_link,
#         'current_year': 2025,
#     }
#     html_message = render_to_string('emails/password_reset_email.html', context)
#     send_mail(subject, "", settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.templatetags.static import static

def send_verification_email(user):
    verification_link = f"{settings.FRONTEND_URL}/#/email-verification?token={user.email_verification_token}"
    subject = 'E-Mail Verifizierung'
    # Nehme an, dein statisches Verzeichnis ist unter https://wilhelm-teicke.developerakademie.net/static/
    # Entferne gegebenenfalls "/videoflix" aus FRONTEND_URL oder passe es an:
    base_url = settings.FRONTEND_URL.replace('/videoflix', '')
    logo_url = "https://wilhelm-teicke.developerakademie.org" + static('logoPNG.png')
    context = {
        'user': user,
        'verification_link': verification_link,
        'current_year': 2025,
        'logo_url': logo_url,
    }
    html_message = render_to_string('emails/verification_email.html', context)
    send_mail(subject, "", settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)

def send_password_reset_email(user):
    reset_link = f"{settings.FRONTEND_URL}/#/password-reset?token={user.password_reset_token}"
    subject = 'Passwort zurücksetzen'
    base_url = settings.FRONTEND_URL.replace('/videoflix', '')
    logo_url = "https://wilhelm-teicke.developerakademie.org" + static('logoPNG.png')
    context = {
        'user': user,
        'reset_link': reset_link,
        'current_year': 2025,
        'logo_url': logo_url,
    }
    html_message = render_to_string('emails/password_reset_email.html', context)
    send_mail(subject, "", settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)
