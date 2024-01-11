from django.core.management.base import BaseCommand

from apps.populate_db import populate_db


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('users_count', type=int, help='Number of users to create')
        parser.add_argument('teams_count', type=int, help='Number of teams to create')

    def handle(self, *args, **options):
        users_count = options['users_count']
        teams_count = options['teams_count']
        populate_db()

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
