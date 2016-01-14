import logging
import sys
import time

from concurrent.futures import ThreadPoolExecutor
from django.core.management.base import BaseCommand
from django.db import connection
from django.utils import timezone
from newrelic import agent

from hc.api.models import Check

executor = ThreadPoolExecutor(max_workers=10)
logger = logging.getLogger(__name__)

agent.initialize()
agent.register_application()


def _stdout(message):
    sys.stdout.write(message)
    sys.stdout.write('\n')
    sys.stdout.flush()


@agent.background_task()
def handle_many():
    """ Send alerts for many checks simultaneously. """
    query = Check.objects.filter(user__isnull=False)

    now = timezone.now()
    going_down = query.filter(alert_after__lt=now, status="up")
    going_up = query.filter(alert_after__gt=now, status="down")
    # Don't combine this in one query so Postgres can query using index:
    checks = list(going_down.iterator()) + list(going_up.iterator())
    if not checks:
        return False

    futures = [executor.submit(handle_one, check) for check in checks]
    for future in futures:
        future.result()

    return True


@agent.background_task()
def handle_one(check):
    """ Send an alert for a single check.

    Return True if an appropriate check was selected and processed.
    Return False if no checks need to be processed.

    """
    check.status = check.get_status()

    tmpl = "Sending alert, status=%s, code=%s\n"
    _stdout(tmpl % (check.status, check.code))

    try:
        check.send_alert()
    except:
        # Catch EVERYTHING. If we crash here, what can happen is:
        # - the sendalerts command will crash
        # - supervisor will respawn sendalerts command
        # - sendalerts will try same thing again, resulting in infinite loop
        # So instead we catch and log all exceptions, and mark
        # the checks as paused so they are not retried.
        agent.record_exception()
        logger.error("Could not alert %s" % check.code, exc_info=True)
        check.status = "paused"
    finally:
        check.save()
        connection.close()

    return True


class Command(BaseCommand):
    help = 'Sends UP/DOWN email alerts'

    def handle(self, *args, **options):
        while True:
            _stdout("Checking alerts")
            handle_many()
            _stdout("Done checking alerts")
            time.sleep(30)
