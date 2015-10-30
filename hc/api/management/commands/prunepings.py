from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from hc.api.models import Check, Ping


class Command(BaseCommand):
    help = 'Prune pings older than one week'

    def handle(self, *args, **options):
        (Check.objects
            .filter(user=None, created__lt=timezone.now() - timedelta(hours=2))
            .delete())

        for check in Check.objects.iterator():
            pings = Ping.objects.filter(owner=check)
            if pings.count() > 20:
                (pings
                    .filter(created__lt=timezone.now() - timedelta(days=7))
                    .delete())
