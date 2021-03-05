from django.core.management.base import BaseCommand, CommandError
from apartments.models import *
from logger.models import ManagementLog
from logger.management_log import Management
from core.tasks import send_notification

class Command(BaseCommand):
    help = "Check for apartment with tenancy less than 3 months"
    title = "Process Tenancy Status"
    log = Management(title)

    def add_arguments(self, parser):
        return super().add_arguments(parser)

    
    def handle(self, *args, **options):
        self.log.in_progress()
        apartments = Apartment.objects.all()

        for index, apartment in enumerate(apartments):
            if apartment.is_occupied:
                days = apartment.time_to_expiry_date()
                if days == 90 or days == 60 or days <=31:
                    apartment.create_reminder(days)

                    self.send_mails()
            self.log.update_count(index + 1)

        self.log.completed()



    def send_mails(self):
        try:
            send_notification.send()
        except:
            raise CommandError('Could not send mail')