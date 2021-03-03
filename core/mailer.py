from django.core.mail import BadHeaderError, message, send_mail, send_mass_mail
from smtplib import SMTPException


def send_tenancy_mail(email, body):
    print(email)
    try: 
        res = send_mail(
            "Tenancy Status Notification",
            body,
            'info@cortts.com',
            [email, 'aminatadetoro@cortts.com', 'info@cortts.com'],
            fail_silently=False,
        )
        print(res)
        return res
    except BadHeaderError as e:
        raise(str(e))
    except SMTPException as e:
        print(e)
        raise(str(e))
