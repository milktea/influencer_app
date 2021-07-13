import logging
import pathlib
import pandas as pd
from typing import Dict, List

from campaigns.models import Campaign, Hashtag
from campaigns.repositories import hashtags as hashtags_repo


logger = logging.getLogger(__name__)


CAMPAIGN_HEADERS = ['name', 'start_date', 'end_date', 'budget', 'team_id', 'description']


def import_campaigns_from_csv(source_file: pathlib.Path):
    """ Note: Source file contains hashtag column. We upload all the hashtags first then
        create a mapping between hashtag name and hashtag object
    :param source_file: campaigns file path
    """
    logger.info(f'Importing campaigns data {source_file}')

    df = pd.read_csv(source_file, sep=',')

    # Add hashtags
    df_hashtags = df['hashtags'].apply(lambda x: x.split(' '))
    unique_hashtag_names = df_hashtags.drop_duplicates().explode().unique()
    hashtags: List[Hashtag] = [Hashtag(name=name) for name in unique_hashtag_names]
    hashtags_repo.bulk_create(hashtags)

    hashtag_name_obj_map = _generate_hashtag_name_obj_map(unique_hashtag_names)

    # Add campaigns
    df_campaigns = df[CAMPAIGN_HEADERS].to_dict(orient='index')

    for index, campaign in df_campaigns.items():
        campaign_obj = Campaign(**campaign)
        campaign_obj.save()

        campaign_hashtags = df_hashtags.loc[index]
        # Attach hashtag/s to campaign
        for hashtag in campaign_hashtags:
            campaign_obj.hashtags.add(hashtag_name_obj_map[hashtag])

    logger.info(f'Campaigns imported successfully.')


def _generate_hashtag_name_obj_map(hashtags_name_list: List[str]) -> Dict[str, Hashtag]:
    """ Fetch hashtag object from hashtags name list and create a map
    :param hashtags_name_list: List of hashtag names
    :return: Dict: hashtag name: hashtags obj map
    """
    hashtags_objs = hashtags_repo.get_hashtags_from_list(hashtags_name_list)
    return {hashtag.name: hashtag for hashtag in hashtags_objs}
