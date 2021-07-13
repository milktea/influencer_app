from datetime import datetime
from campaigns import constants


def format_date_to_str(value: datetime) -> str:
    return value.strftime(constants.DATE_TIME_FORMAT)
