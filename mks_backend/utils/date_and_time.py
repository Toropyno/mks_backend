from typing import Optional

from datetime import date as Date
from datetime import datetime as DateTime


def get_date_string(date: Date) -> Optional[str]:
    return date.strftime('%Y,%m,%d') if date else None


def get_date_time_string(date_time: DateTime) -> Optional[str]:
    return date_time.strftime('%d.%m.%Y %H:%M:%S') if date_time else None


def get_date_time_zone(date_time: DateTime) -> str:
    return date_time.strftime('%d.%m.%Y %H:%M:%S %Z')