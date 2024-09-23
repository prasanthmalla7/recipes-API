'''django command to wait for db'''
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''django command to wait for db'''

    def handle(self, *args, **options):
        self.stdout.write("waiting for db...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(' DB unavailable, waiting 1 second ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB is available!'))
