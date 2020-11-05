import re
from datetime import datetime

import colander


def date_validator(node: colander.SchemaNode, date: str) -> None:
    try:
        date = datetime.strptime(date, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def uuid_file_validator(node: colander.SchemaNode, value: str) -> None:
    uuid_validator('Недопустимая информация о файле', node, value)


def uuid_aoid_validator(node: colander.SchemaNode, value: str) -> None:
    uuid_validator('Недопустимая информация о aoid', node, value)


def uuid_validator(message, node, value):
    pattern = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    res = re.match(pattern, value)
    if res is None:
        raise colander.Invalid(node, message)


def strip_space(value: str) -> str:
    if value:
        value = value.strip(' \t\n\r')
    return value


def timestamp_validator(node: colander.SchemaNode, date_time: str) -> None:
    try:
        date_time = datetime.strptime(date_time, '%a %b %d %Y %H:%M:%S')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты и времени')
