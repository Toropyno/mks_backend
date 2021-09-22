import re
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


def phone_validator(node: colander.SchemaNode, value: str) -> None:
    pattern = r'\\+?[\d\s\\-\\(\\)]{3,40}'
    validator_by_pattern(node, value, pattern)


def email_validator(node: colander.SchemaNode, value: str) -> None:
    pattern = r'[\da-zA-ZА-ЯЁа-яё\\-\\_]+@[\da-zA-ZА-ЯЁа-яё\\-\\_]+\\.[a-zA-ZА-ЯЁа-яё]+'
    validator_by_pattern(node, value, pattern)


def validator_by_pattern(node: colander.SchemaNode, value: str, pattern: str) -> None:
    res = re.fullmatch(pattern, value)
    if res is None or len(value) > 80:
        raise colander.Invalid(node, node.msg)
