import logging
from typing import List

from campaigns.models import Hashtag
from campaigns import constants

logger = logging.getLogger(__name__)


def bulk_create(objs_list: List[Hashtag],
                batch_size: int = constants.DEFAULT_BATCH_SIZE):
    logger.debug('Creating bulk hashtags')
    Hashtag.objects.bulk_create(objs_list, batch_size, ignore_conflicts=True)


def get_hashtags_from_list(hashtags_list: List[str]) -> List[Hashtag]:
    logger.debug('Fetching hashtag objects from list of hashtag names')
    return Hashtag.objects.filter(name__in=hashtags_list)


def delete_all():
    logger.debug('Deleting all hashtags')
    Hashtag.objects.all().delete()
