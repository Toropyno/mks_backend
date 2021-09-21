from datetime import datetime, timedelta
from random import randint

from faker import Faker
from sqlalchemy.exc import DBAPIError

from mks_backend.session import DBSession


def get_random_address():
    fake = Faker('ru_RU')
    return fake.address()


def get_rand_int():
    return str(randint(10000000, 99999999))


def get_random_date():
    start = datetime.strptime('1/1/1990 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('12/12/2020 4:50 AM', '%m/%d/%Y %I:%M %p')

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    for random_second in range(0, int_delta, 86400):
        result = start + timedelta(seconds=random_second)
        yield result


def get_random_name() -> str:
    fake = Faker('ru_RU')
    return fake.name()


def get_first_name() -> str:
    """
    Получить имя
    """
    fake = Faker('ru_RU')
    return fake.first_name_male()


def get_surname() -> str:
    """
    Получить фамилию
    """
    fake = Faker('ru_RU')
    return fake.last_name_male()


def get_middle_name() -> str:
    """
    Получить отчество
    """
    fake = Faker('ru_RU')
    return fake.middle_name_male()


def get_random_phone() -> str:
    return Faker('ru_RU').phone_number()


def get_random_email() -> str:
    return Faker().ascii_email()


def try_add(instance):
    try:
        DBSession.add(instance)
        DBSession.commit()
    except DBAPIError:
        DBSession.rollback()
