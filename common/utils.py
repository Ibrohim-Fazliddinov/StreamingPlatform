from django.core.mail import send_mail
from django.conf import settings


def send_password_change_notification(email):
    subject = 'Уведомление о смене пароля'
    message = 'Ваш пароль был успешно изменен. Если это не вы сделали, пожалуйста, свяжитесь с нашей службой поддержки.'
    from_email = settings.EMAIL_HOST_USER

    send_mail(
        subject,
        message,
        from_email,
        [email],
        fail_silently=False,
    )
