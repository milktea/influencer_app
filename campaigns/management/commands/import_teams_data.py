import pathlib
from django.core.management.base import BaseCommand

from campaigns.services import teams as teams_service


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('src', type=pathlib.Path, help='Source file path')

    def handle(self, *args, **options):
        source_file = options['src']
        teams_service.import_teams_from_csv(source_file)
