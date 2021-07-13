import pytest
from typing import Dict, List
from http import HTTPStatus


from django.urls import reverse
from rest_framework.test import APIClient

from campaigns.models import Campaign


@pytest.mark.django_db
def test_campaigns_api_with_no_data():
    """ Test fetching empty campaigns data,
        Should return status ok and an empty list
    """
    client = APIClient()
    result = client.get(reverse('campaigns-list'))
    assert result.status_code == HTTPStatus.OK

    data: List[Dict] = result.data
    assert len(data) == 0


@pytest.mark.django_db
def test_campaigns_api_with_data(campaign_data: Campaign):
    """ Test campaigns api list,
        returning one campaign and hashtag data
    """
    client = APIClient()
    result = client.get(reverse('campaigns-list'))
    assert result.status_code == HTTPStatus.OK

    data: List[Dict] = result.data
    assert len(data) == 1

    result_campaign = data[0]

    # check campaign data
    assert result_campaign['name'] == campaign_data.name

    # check campaign team
    assert result_campaign['team']['name'] == campaign_data.team.name

    # check campaign hashtags
    result_campaign_hashtags = result_campaign['hashtags']
    expected_campaign_hashtags = campaign_data.hashtags.all()
    assert len(result_campaign['hashtags']) == len(expected_campaign_hashtags)
    assert result_campaign_hashtags[0]['name'] == expected_campaign_hashtags[0].name
