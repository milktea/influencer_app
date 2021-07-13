import pathlib

from django.core.management.base import BaseCommand
from campaigns.services import campaigns as campaigns_service


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('src', type=pathlib.Path, help='Source file path')

    def handle(self, *args, **options):
        source_file = options['src']
        campaigns_service.import_campaigns_from_csv(source_file)
