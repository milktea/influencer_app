from rest_framework import viewsets

from campaigns.repositories import campaigns as campaigns_repo
from campaigns.serializers.campaigns import CampaignSerializer


class CampaignView(viewsets.ModelViewSet):
    queryset = campaigns_repo.get_campaigns_with_hashtags()
    serializer_class = CampaignSerializer
