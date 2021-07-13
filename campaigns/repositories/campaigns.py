import logging
from typing import List

from campaigns.models import Campaign


logger = logging.getLogger(__name__)


def bulk_create(objs_list: List[Campaign], batch_size: int = 500):
    logger.debug('Creating campaigns in bulk')
    Campaign.objects.bulk_create(objs_list, batch_size, ignore_conflicts=True)


def get_campaigns_with_hashtags() -> List[Campaign]:
    logger.debug('Getting campaigns with hashtags')
    return Campaign.objects.all().prefetch_related('hashtags')


def delete_all():
    logger.debug('Deleting all campaigns')
    Campaign.objects.all().delete()
