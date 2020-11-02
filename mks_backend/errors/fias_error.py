from pyramid.response import Response


class FIASError(Exception):
    codes = {
        'cannotFindAddress': 'Адрес не найден',
        'notFindAOID': 'Не заполнен aoid',
        'notFindCityLocality': 'Адрес не найден: необходимы город или поселение',
    }

    def __init__(self, code: str):
        self.code = code
        self.msg = self.codes[code]


def fias_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except TypeError:
            return Response(
                status=100,
                json_body=get_extract_addresses_error()
            )

        except KeyError:
            return Response(
                status=100,
                json_body=get_fiasapi_search_error()
            )

    return wrapper


def get_fiasapi_search_error() -> dict:
    return {'code': 'fiasapiCannotFindSentence', 'message': 'Ошибка от стороннего fiasapi: Не найдено вариантов'}


def get_extract_addresses_error() -> dict:
    return {'code': 'extractAddressesError', 'message': 'Не удалось извлечь адреса из ответа стороннего fiasapi'}
