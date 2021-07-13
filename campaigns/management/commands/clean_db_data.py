import logging
from django.core.management.base import BaseCommand

from campaigns.repositories import campaigns as campaigns_repo
from campaigns.repositories import hashtags as hashtags_repo
from campaigns.repositories import teams as teams_repo


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        campaigns_repo.delete_all()
        logger.info(f'Campaigns deleted.')

        hashtags_repo.delete_all()
        logger.info(f'Hashtags deleted.')

        teams_repo.delete_all()
        logger.info(f'Teams deleted.')
