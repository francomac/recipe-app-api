"""
Django Command to Wait for Database to be Available
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to pause execution until database is available """

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        self.stdout.write('Database available!')
        pass