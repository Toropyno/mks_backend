from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .. import models

try:
    Session = sessionmaker(bind=create_engine('postgresql://yan:yan@172.23.112.98:5432/mks_db'),
                           autocommit=False,
                           autoflush=False)
    session = Session()
except DBAPIError:
    print('ERROR WITH DB')


@view_config(route_name='protocols', request_method='GET', renderer='json')
def protocols_view(request):
    """
    Return protocols
    """
    if request.params:
        # filtration params
        pass
    else:
        # protocols = protocol_query.all()
        protocols = session.query(models.Protocol).all()
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


@view_config(route_name='add_protocol', request_method='GET', renderer='json')
def get_meetings_types_view(request):
    meetings_query = session.query(models.Meeting)
    return [meeting.meetings_type_id for meeting in meetings_query.all()]


@view_config(route_name='add_protocol', request_method='POST', renderer='json')
def add_protocol_view(request):
    recieved_data = dict(request.POST.items())
    new_protocol = models.Protocol(protocol_num=recieved_data.get('protocol_num'),
                                   protocol_date=recieved_data.get('protocol_date'),
                                   meetings_type_id=recieved_data.get('meetings_type_id'),
                                   protocol_name=recieved_data.get('protocol_name'),
                                   note=recieved_data.get('note'),
                                   idfilestorage=recieved_data.get('idfilestorage'))
    #  TODO: add file uploading mechanism
    session.add(new_protocol)
    session.commit()
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
