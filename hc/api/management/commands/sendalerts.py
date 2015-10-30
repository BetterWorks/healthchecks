import sys
import time

from django.core.management.base import BaseCommand
from django.utils import timezone

from hc.api.models import Check


def _log(message):
    sys.stdout.write(message)
    sys.stdout.flush()


class Command(BaseCommand):
    help = 'Sends UP/DOWN email alerts'

    def handle(self, *args, **options):
        while True:
            # Gone down?
            query = Check.objects
            query = query.filter(alert_after__lt=timezone.now())
            query = query.filter(user__isnull=False)
            query = query.filter(status="up")
            for check in query.iterator():
                check.status = "down"

                _log(
                    "\nSending notification(s) about going down for %s\n" %
                    check.code)
                try:
                    check.send_alert()

                    # Save status after the notification is sent
                    check.save()
                except:
                    _log(
                        '\nError sending notification(s) for %s\n' %
                        check.code)

            # Gone up?
            query = Check.objects
            query = query.filter(alert_after__gt=timezone.now())
            query = query.filter(user__isnull=False)
            query = query.filter(status="down")
            for check in query.iterator():
                check.status = "up"

                _log(
                    "\nSending notification(s) about going up for %s\n" %
                    check.code)
                try:
                    check.send_alert()

                    # Save status after the notification is sent
                    check.save()
                except:
                    _log(
                        '\nError sending notification(s) for %s\n' %
                        check.code)

            time.sleep(30)
