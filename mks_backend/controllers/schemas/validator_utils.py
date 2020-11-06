import re
from typing import Optional
from datetime import datetime

import colander


def date_validator(node: colander.SchemaNode, date: str) -> None:
    try:
        date = datetime.strptime(date, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def organization_parent_uuid(node: colander.SchemaNode, value: str):
    if uuid_validator(value) is None:
        raise colander.Invalid(node, 'Такой организации-родителя не существует')


def uuid_file_validator(node: colander.SchemaNode, value: str) -> None:
    if uuid_validator(value) is None:
        raise colander.Invalid(node, 'Недопустимая информация о файле')


def uuid_validator(value: str) -> Optional[re.Match]:
    pattern = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    return re.match(pattern, value)


def strip_space(value: str) -> str:
    if value:
        value = value.strip(' \t\n\r')
    return value


def timestamp_validator(node: colander.SchemaNode, date_time: str) -> None:
    try:
        date_time = datetime.strptime(date_time, '%a %b %d %Y %H:%M:%S')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты и времени')
