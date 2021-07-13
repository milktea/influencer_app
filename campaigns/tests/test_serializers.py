import pytest
from collections import OrderedDict

from campaigns import utils
from campaigns.models import Campaign, Hashtag, Team
from campaigns.serializers.campaigns import CampaignSerializer
from campaigns.serializers.hashtags import HashtagSerializer
from campaigns.serializers.teams import TeamSerializer


@pytest.mark.django_db
def test_team_serializer(team_data: Team):
    serialized_data = TeamSerializer(team_data).data
    assert serialized_data == {
        'id': team_data.id,
        'name': team_data.name,
        'code': team_data.code,
        'color_set': team_data.color_set,
    }


@pytest.mark.django_db
def test_hashtag_serializer(hashtag_data: Hashtag):
    serialized_data = HashtagSerializer(hashtag_data).data
    assert serialized_data == {
        'id': hashtag_data.id,
        'name': hashtag_data.name,
    }


@pytest.mark.django_db
def test_campaign_serializer(campaign_data: Campaign):
    serialized_data = CampaignSerializer(campaign_data).data
    campaign_data_hashtags = campaign_data.hashtags.all()

    assert serialized_data == {
        'id': campaign_data.id,
        'budget': f'${campaign_data.budget:,.2f}',
        'start_date': utils.format_date_to_str(campaign_data.start_date),
        'end_date': utils.format_date_to_str(campaign_data.start_date),
        'hashtags': [
            OrderedDict({'id': campaign_data_hashtags[0].id,
                         'name': campaign_data_hashtags[0].name})
        ],
        'team': OrderedDict({
            'id': campaign_data.team.id,
            'name': campaign_data.team.name,
            'code': campaign_data.team.code,
            'color_set': campaign_data.team.color_set,
        }),
        'name': campaign_data.name,
        'description': campaign_data.description,
    }
