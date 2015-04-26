"""
This command deletes older Log entries
"""
from __future__ import absolute_import

from optparse import make_option
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...models import Log

import logging

logger = logging.getLogger('monitoring')

DEFAULT_TIMEDELTA_DAYS = 30  # Keep Log entries for 30 days


class Command(BaseCommand):
    args = 'keep-delta'
    help = 'Deletes older Log entries.'
    option_list = BaseCommand.option_list + (
        make_option('--verbose',
                    action='store_true',
                    dest='verbose',
                    default=False,
                    help='Print progress on command line'),
    )

    def handle(self, *args, **options):
        """
        Delete older Log entries.
        """
        verbose = options['verbose']

        if args and args[0].isdigit():
            timedelta_days = int(args[0])
            if verbose:
                print('Delete Log entries to older than %d days)' % (timedelta_days))
        else:
            timedelta_days = DEFAULT_TIMEDELTA_DAYS

        delete_before = timezone.now() - timedelta(days=timedelta_days)

        if verbose:
            log_count = Log.objects.filter(datetime__lt=delete_before).count()
            print('%d Log entries to delete (older than %s)' % (log_count, delete_before))

        Log.objects.filter(datetime__lt=delete_before).delete()

        if verbose:
            logger.info('Log entries deleted successfully')
