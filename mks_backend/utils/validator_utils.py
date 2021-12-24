from uuid import UUID
from datetime import datetime

import colander


def date_validator(node: colander.SchemaNode, date: str) -> None:
    try:
        datetime.strptime(date, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def timestamp_validator(node: colander.SchemaNode, date_time: str) -> None:
    try:
        datetime.strptime(date_time, '%a %b %d %Y %H:%M:%S')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты и времени')


def strip_space(value: str) -> str:
    if value:
        value = value.strip(' \t\n\r')
    return value


def organization_parent_uuid(node: colander.SchemaNode, value: str):
    if not is_uuid(value):
        raise colander.Invalid(node, 'Такой организации-родителя не существует')


def organization_uuid(node: colander.SchemaNode, value: str):
    if not is_uuid(value):
        raise colander.Invalid(node, 'Такой организации не существует')


def uuid_file_validator(node: colander.SchemaNode, value: str) -> None:
    if not is_uuid(value):
        raise colander.Invalid(node, 'Недопустимая информация о файле')


def is_uuid(value: str) -> bool:
    try:
        UUID(value)
    except ValueError:
        return False
    else:
        return True
