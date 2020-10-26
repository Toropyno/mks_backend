def fias_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return []

    return wrapper


def get_addition_fias_error_dict() -> dict:
    return {'code': 'NotFullAddress', 'message': 'Адрес заполнен не полностью'}


def get_locality_error_dict() -> dict:
    return {'code': 'NotFullAddress', 'message': 'Заполните город или поселение'}


def get_remaining_address_error_dict() -> dict:
    return {'code': 'NotFullAddress', 'message': 'Не заполнена улица'}
