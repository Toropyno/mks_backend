from datetime import date as Date
from datetime import datetime as DateTime
from typing import Optional


def get_date_string(date: Date) -> Optional[str]:
    return date.strftime('%Y,%m,%d') if date else None


def get_date_time_string(date_time: DateTime) -> Optional[str]:
    return date_time.strftime('%d.%m.%Y %H:%M:%S') if date_time else None


def get_date_time_zone(date_time: DateTime) -> str:
    return date_time.strftime('%d.%m.%Y %H:%M:%S %Z')


def get_date_iso_string(date: Date) -> Optional[str]:
    """
    :param date: datetime
    :return: str строка даты в ISO формате, например: 2002-12-04
    """
    return date.isoformat() if date else None


def get_date_time_from_string(date: str) -> Optional[Date]:
    """
    :param date: str строка даты в ISO формате, например: 2002-12-04
    :return: DateTime
    """
    return DateTime.strptime(date, '%a %b %d %Y').date() if date else None
