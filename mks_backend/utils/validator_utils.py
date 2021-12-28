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


def inn_validator(node: colander.SchemaNode, value: str) -> None:
    if not value.isdigit():
        raise colander.Invalid(node, 'ИНН некорректен - он может состоять только из цифр')

    if len(value) == 10:
        check_digit = ((2 * int(value[0]) +
                        4 * int(value[1]) +
                        10 * int(value[2]) +
                        3 * int(value[3]) +
                        5 * int(value[4]) +
                        9 * int(value[5]) +
                        4 * int(value[6]) +
                        6 * int(value[7]) +
                        8 * int(value[8])) % 11) % 10
        if int(value[-1]) != check_digit:
            raise colander.Invalid(node, 'ИНН некорректен - контрольное число не прошло проверку')

    elif len(value) == 12:
        first_check_digit = ((7 * int(value[0]) +
                              2 * int(value[1]) +
                              4 * int(value[2]) +
                              10 * int(value[3]) +
                              3 * int(value[4]) +
                              5 * int(value[5]) +
                              9 * int(value[6]) +
                              4 * int(value[7]) +
                              6 * int(value[8]) +
                              8 * int(value[9])) % 11) % 10

        second_check_digit = ((3 * int(value[0]) +
                               7 * int(value[1]) +
                               2 * int(value[2]) +
                               4 * int(value[3]) +
                               10 * int(value[4]) +
                               3 * int(value[5]) +
                               5 * int(value[6]) +
                               9 * int(value[7]) +
                               4 * int(value[8]) +
                               6 * int(value[9]) +
                               8 * int(value[10])) % 11) % 10

        if int(value[-1]) != first_check_digit and int(value[-2]) != second_check_digit:
            raise colander.Invalid(node, 'ИНН некорректен - контрольное число не прошло проверку')

    else:
        raise colander.Invalid(node, 'ИНН некорректен - он может состоять только из 10 или 12 цифр')


def kpp_validator(node: colander.SchemaNode, value: str) -> None:
    if not value.isdigit() or len(value) != 9:
        raise colander.Invalid(node, 'КПП некорректен - он может состоять только из 9 цифр')


def ogrn_validator(node: colander.SchemaNode, value: str) -> None:
    if not value.isdigit():
        raise colander.Invalid(node, 'ОГРН некорректен - он может состоять только из цифр')

    if len(value) == 13:
        remainder = str(int(value[:-1]) % 11)
        if value[-1] != remainder[-1]:
            raise colander.Invalid(node, 'ОГРН некорректен - контрольное число не прошло проверку')

    elif len(value) == 15:
        remainder = str(int(value[:-1]) % 13)
        if value[-1] != remainder[-1]:
            raise colander.Invalid(node, 'ОГРН некорректен - контрольное число не прошло проверку')

    else:
        raise colander.Invalid(node, 'ОГРН некорректен - он может состоять только из 13 или 15 цифр')


def is_uuid(value: str) -> bool:
    try:
        UUID(value)
    except ValueError:
        return False
    else:
        return True
