import logging

from pyramid.httpexceptions import HTTPForbidden
from webob import Response
from pyramid.view import view_config
from colander import Invalid as ColanderInvalid
from sqlalchemy.exc import DBAPIError

from . import DBBasicError, FilestorageError
from mks_backend.session import DBSession


@view_config(context=DBAPIError)
def db_api_error(context, request):
    DBSession.rollback()

    if context.orig.pgerror:
        # Если есть текст ошибки от БД, то бросаем новую, и приводим к нужному формату
        raise DBBasicError(context.orig.pgerror)
    else:
        # Когда текста ошибки от БД нет, значит, мы даже не смогли к ней подключиться
        message = context.orig.args[0].strip() if context.orig.args else 'Не удалось подключиться к БД'
        return HTTPForbidden(json_body={'code': 'unauthorized', 'message': message})


@view_config(context=DBBasicError)
def db_error_exception_view(context, request):
    DBSession.rollback()
    return Response(status=400, json_body=context.code_and_message)


@view_config(context=FilestorageError)
def filestorage_exception_view(context, request):
    return Response(status=403, json_body={'code': context.code, 'message': context.msg})


@view_config(context=ColanderInvalid)
def colander_exception_view(context, request):
    def get_collander_error_dict(errors: dict) -> dict:
        return {'code': list(errors.keys()).pop(), 'message': '.\n\n'.join(errors.values())}

    return Response(status=403, json_body=get_collander_error_dict(context.asdict()))


@view_config(context=HTTPForbidden)
def unauthorized(context, request):
    message = 'Недостаточно прав для просмотра ресурса' if 'Unauthorized' in context.detail else context.detail
    return Response(status=403, json_body={'code': 'unauthorized', 'message': message})


@view_config(context=Exception)
def exception_view(context, request):
    logging.info(context)
    return Response(status=500, json_body={'code': 'something goes wrong', 'message': 'Что-то пошло не так'})
