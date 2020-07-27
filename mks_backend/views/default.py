from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name='protocols', renderer='json')
def protocols_view(request):
    """
    Return protocols
    """
    try:
        protocol_query = request.dbsession.query(models.Protocol)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    if request.method == 'GET':
        if request.params:
            # filtration params
            pass
        else:
            protocols = protocol_query.all()
            return protocols


@view_config(route_name='protocols_delete_and_view', renderer='json')
def protocols_delete_and_view(request):
    """
    Delete protocol
    """
    if request.method == 'DELETE':
        protocol_query = request.dbsession.query(models.Protocol)
        protocol_to_delete = protocol_query.filter(models.Protocol.protocol_id == request.matchdict['id'])
        if protocol_to_delete.delete():
            return True
        else:
            return False
    if request.method == 'GET':
        protocols_query = request.dbsession.query(models.Protocol)
        protocol_to_view = protocols_query.filter(models.Protocol.protocol_id == request.matchdict['id'])
        if protocol_to_view.first() is None:
            return False
        else:
            return protocol_to_view.first()



db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
