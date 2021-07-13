from datetime import datetime
from rest_framework import serializers

from campaigns import utils


class CustomDateTimeFieldSerializer(serializers.DateTimeField):
    def to_representation(self, value: datetime) -> str:
        return utils.format_date_to_str(value)
