import pytest
from datetime import datetime

from campaigns.models import Campaign, Hashtag, Team


@pytest.fixture()
def team_data() -> Team:
    """ Sample team data """
    team = Team(name="Team")
    team.save()
    return team


@pytest.fixture()
def hashtag_data() -> Hashtag:
    """ Sample hashtag data """
    hashtag = Hashtag(name="hashtag")
    hashtag.save()
    return hashtag


@pytest.fixture()
def campaign_data(team_data: Team, hashtag_data: Hashtag) -> Campaign:
    """ Sample campaign data """
    campaign = Campaign(
        name="Campaign",
        description="description",
        budget=1000.00,
        start_date=datetime.now(),
        end_date=datetime.now(),
        team=team_data,
    )
    campaign.save()
    campaign.hashtags.add(hashtag_data)
    return campaign
