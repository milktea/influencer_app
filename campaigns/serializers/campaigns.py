from rest_framework import serializers

from campaigns.models import Campaign

from campaigns.serializers.hashtags import HashtagSerializer
from campaigns.serializers.teams import TeamSerializer
from campaigns.serializers.utils import CustomDateTimeFieldSerializer


class CampaignSerializer(serializers.ModelSerializer):
    budget = serializers.SerializerMethodField()
    start_date = CustomDateTimeFieldSerializer()
    end_date = CustomDateTimeFieldSerializer()

    hashtags = HashtagSerializer(many=True)
    team = TeamSerializer()

    @staticmethod
    def get_budget(obj: Campaign) -> str:
        # format dollar sign with thousands comma separator and two decimal places
        return f'${obj.budget:,.2f}'

    class Meta:
        model = Campaign
        fields = '__all__'
