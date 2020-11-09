import re
from datetime import datetime

import colander


def date_validator(node: colander.SchemaNode, date: str) -> None:
    try:
        date = datetime.strptime(date, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def strip_space(value: str) -> str:
    if value:
        value = value.strip(' \t\n\r')
    return value


def timestamp_validator(node: colander.SchemaNode, date_time: str) -> None:
    try:
        date_time = datetime.strptime(date_time, '%a %b %d %Y %H:%M:%S')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты и времени')


def uuid_validator(node: colander.SchemaNode, value: str) -> None:
    pattern = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    validator_by_regular(node, pattern, value)


def validator_by_regular(node, pattern, value):
    res = re.match(pattern, value)
    if res is None:
        raise colander.Invalid(node, node.msg)


def phone_validator(node: colander.SchemaNode, value: str) -> None:
    pattern = '[0-9s\\-\\(\\)]+{3,40}'
    res = re.match(pattern, value)
    if res is None:
        raise colander.Invalid(node, node.msg)


def email_validator(node: colander.SchemaNode, value: str) -> None:
    pattern = '[^@\s]+@[^@\s]+\.[^@\s]+'
    res = re.match(pattern, value)
    if res is None:
        raise colander.Invalid(node, node.msg)
