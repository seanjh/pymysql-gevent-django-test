import random

from django.core.management.base import BaseCommand
from django.db import connection

import gevent

WAIT_SECS = 1


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('letters', nargs='+')

    def handle(self, *args, **options):
        tasks = [
            gevent.spawn(self.get_filler, letter)
            for letter in options['letters']
        ]

        gevent.joinall(tasks, raise_error=True)
        # gevent.wait()

    def get_filler(self, letter):
        wait = random.random() * WAIT_SECS
        self.stdout.write('Fetch filler for "{}" with {:0.4f} wait'
                          .format(letter, wait))

        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT SLEEP(%s), id
                FROM testapp_filler
                WHERE LOCATE(%s, thing_one)
                AND LOCATE(%s, thing_two)
                LIMIT 5
                """, [wait, letter, letter])
            results = cursor.fetchall()

        self.stdout.write('Retrieved {:,d} filler objects for "{}"'
                          .format(len(list(results)), letter))
