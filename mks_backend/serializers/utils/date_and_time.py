from datetime import date as Date
from datetime import datetime as DateTime


def get_date_string(date: Date) -> str:
    if date:
        return date.strftime('%Y,%m,%d')


def get_date_time_string(date_time: DateTime) -> str:
    if date_time:
        return date_time.strftime('%d.%m.%Y %H:%M:%S')


def get_date_time_zone(date_time: DateTime) -> str:
    return date_time.strftime('%d.%m.%Y %H:%M:%S %Z')
