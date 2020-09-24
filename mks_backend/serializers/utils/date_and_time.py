from datetime import date as Date
from datetime import datetime as DateTime


def get_date_string(date: Date) -> str:
    return str(date.year) + ',' + str(date.month) + ',' + str(date.day)


def get_date_time_string(date_time: DateTime) -> str:
    return str(date_time.day) + '.' + str(date_time.month) + '.' + str(date_time.year) + \
           ' ' + str(date_time.hour) + ':' + str(date_time.minute) + ':' + str(date_time.second)