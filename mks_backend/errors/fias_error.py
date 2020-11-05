from pyramid.response import Response


class FIASError(Exception):
    codes = {
        'cannotFindAddress': 'Адрес не найден',
        'notFindAOID': 'Не заполнен aoid',
        'notFindCityLocality': 'Адрес не найден: необходимы город или поселение',
        'notFilledAddress': 'Не заполнен адрес',
        'extractAddressesError': 'Не удалось извлечь адреса из ответа стороннего fiasapi'
    }

    def __init__(self, code: str):
        self.code = code
        self.msg = self.codes[code]


def fias_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except AttributeError:
            return Response(
                status=403,
                json_body={
                    'code': 'fiasapiCannotFindSentence',
                    'message': 'Ошибка от стороннего fiasapi: Не найдено вариантов',
                }
            )

    return wrapper
