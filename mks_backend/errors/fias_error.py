from pyramid.response import Response


def fias_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except TypeError:
            return Response(
                status=403,
                json_body=get_extract_addresses_error()
            )

        except KeyError:
            return Response(
                status=403,
                json_body=get_fiasapi_search_error()
            )

    return wrapper


def get_addition_fias_error() -> Response:
    body = {'code': 'notFullAddress', 'message': 'Адрес заполнен не полностью'}
    return Response(
        status=403,
        json_body=body
    )


def get_locality_error() -> Response:
    body = {'code': 'notFindCityLocality', 'message': 'Заполните город или поселение'}
    return Response(
        status=403,
        json_body=body
    )


def get_remaining_address_error() -> Response:
    body = {'code': 'notFindStreet', 'message': 'Не заполнена улица'}
    return Response(
        status=403,
        json_body=body
    )


def get_aoid_error() -> Response:
    body = {'code': 'notFindAOID', 'message': 'Не заполнен aoid'}
    return Response(
        status=403,
        json_body=body
    )


def get_cannot_find_address_error() -> Response:
    body = {'code': 'cannotFindAddress', 'message': 'Адрес не найден'}
    return Response(
        status=403,
        json_body=body
    )


def get_fiasapi_search_error() -> dict:
    return {'code': 'fiasapiCannotFindSentence', 'message': 'Ошибка от стороннего fiasapi: Не найдено вариантов'}


def get_extract_addresses_error() -> dict:
    return {'code': 'extractAddressesError', 'message': 'Не удалось извлечь адреса из ответа стороннего fiasapi'}
