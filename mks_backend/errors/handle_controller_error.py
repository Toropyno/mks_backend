from colander import Invalid as ColanderInvalid
from pyramid.response import Response

from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError


def handle_colander_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ColanderInvalid as error:
            return Response(
                status=403,
                json_body=get_collander_error_dict(error.asdict())
            )

    return wrapper


def handle_db_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

    return wrapper
