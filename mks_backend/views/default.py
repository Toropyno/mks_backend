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


@view_config(route_name='add_protocol', renderer='json')
def add_protocol_view(request):
    try:
        protocol_query = request.dbsession.query(models.Protocol)
        meetings_query = request.dbsession.query(models.Meeting)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    if request.method == 'GET':
        return [meeting.meetings_type_id for meeting in meetings_query.all()]
    elif request.method == 'POST':
        recieved_data = dict(request.POST.items())

        new_protocol = models.Protocol(protocol_num=recieved_data.get('protocol_num'),
                                       protocol_date=recieved_data.get('protocol_date'),
                                       meetings_type_id=recieved_data.get('meetings_type_id'),
                                       protocol_name=recieved_data.get('protocol_name'),
                                       note=recieved_data.get('note'),
                                       idfilestorage=recieved_data.get('idfilestorage'),
                                       )
        protocol_query.session.add(new_protocol)
        protocol_query.session.flush()

        return new_protocol.protocol_id


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
