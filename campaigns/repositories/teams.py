import logging
from typing import List

from campaigns.models import Team
from campaigns import constants

logger = logging.getLogger(__name__)


def bulk_create(objs_list: List[Team],
                batch_size: int = constants.DEFAULT_BATCH_SIZE):
    logger.debug('Creating bulk teams')
    Team.objects.bulk_create(objs_list, batch_size, ignore_conflicts=True)


def get_teams_from_list(teams_list: List[str]) -> List[Team]:
    logger.debug('Fetching hashtags from list')
    return Team.objects.filter(name__in=teams_list)


def delete_all():
    logger.debug('Deleting all teams')
    Team.objects.all().delete()
