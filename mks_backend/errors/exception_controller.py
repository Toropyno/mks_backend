from webob import Response
from pyramid.view import view_config
from colander import Invalid as ColanderInvalid
from sqlalchemy.exc import DBAPIError

from . import DBBasicError, FilestorageError
from mks_backend.session import DBSession


@view_config(context=DBAPIError)
def db_api_error(context, request):
    DBSession.rollback()
    raise DBBasicError(context.orig.pgerror)


@view_config(context=DBBasicError)
def db_error_exception_view(context, request):
    return Response(status=403, json_body=context.code_and_message)


@view_config(context=FilestorageError)
def filestorage_exception_view(context, request):
    return Response(status=403, json_body={'code': context.code, 'message': context.msg})


@view_config(context=ColanderInvalid)
def colander_exception_view(context, request):
    def get_collander_error_dict(errors: dict) -> dict:
        return {'code': list(errors.keys()).pop(), 'message': '.\n\n'.join(errors.values())}

    return Response(status=403, json_body=get_collander_error_dict(context.asdict()))


@view_config(context=Exception)
def exception_view(context, request):
    return Response(status=500, json_body={'code': 'something goes wrong', 'message': 'Что-то пошло не так'})
