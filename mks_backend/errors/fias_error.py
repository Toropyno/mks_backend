def fias_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return []

    return wrapper


def get_fias_error_dict() -> dict:
    return {'code': 'NotFullAddress', 'message': 'Адрес заполнен не полностью'}
