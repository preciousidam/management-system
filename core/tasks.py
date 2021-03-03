import dramatiq

from apartments.models import Reminder
from .mailer import send_tenancy_mail


@dramatiq.actor
def send_notification():
    reminders = Reminder.objects.all()

    for reminder in reminders:
        if reminder.active:
            email = reminder.apartment.tenant.email
            body = reminder.body
            send_tenancy_mail(email, body)
            reminder.active = False
            reminder.save()
            