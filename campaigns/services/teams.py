import logging
import pathlib
from typing import List
import pandas as pd


from campaigns.models import Team
from campaigns.repositories import teams as teams_repo


logger = logging.getLogger(__name__)


def import_teams_from_csv(source_file: pathlib.Path):
    """ Import teams (team name should be unique)
    :param source_file: teams file path
    """
    logger.info(f'Importing teams data {source_file}')
    df = pd.read_csv(source_file, sep=',')
    df = df.to_dict(orient='index')

    teams: List[Team] = [Team(**v) for _, v in df.items()]
    teams_repo.bulk_create(teams)

    logger.info(f'Teams imported successfully.')
