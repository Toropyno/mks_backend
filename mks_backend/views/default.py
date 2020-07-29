import shutil
import os
import urllib
from uuid import uuid4

from pyramid.view import view_config
from pyramid.response import FileResponse, Response

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .. import models


PROTOCOLS_STORAGE = '/tmp/protocols'

try:
    Session = sessionmaker(bind=create_engine('postgresql://yan:yan@172.23.112.98:5432/mks_db'),
                           autocommit=False,
                           autoflush=False)
    session = Session()
except DBAPIError:
    print('ERROR WITH DB')


@view_config(route_name='protocols', request_method='GET', renderer='json')
def protocols_view(request):
    if request.params:
        params = dict(request.params)
        protocols = session.query(models.Protocol)
        filter_dict = dict(zip(params.keys(), params.values()))
        return protocols.filter_by(**filter_dict).all()
    else:
        protocols = session.query(models.Protocol).all()
        return protocols


@view_config(route_name='protocols_delete_change_and_view', request_method='GET', renderer='json')
def protocol_view(request):
    protocols_query = session.query(models.Protocol)
    protocol_to_view = protocols_query.filter_by(protocol_id=request.matchdict['id']).first()
    if protocol_to_view is None:
        return False
    else:
        return protocol_to_view


@view_config(route_name='protocols_delete_change_and_view', request_method='DELETE', renderer='json')
def delete_protocol_view(request):
    protocol_query = session.query(models.Protocol)
    protocol_to_delete = protocol_query.filter_by(protocol_id=request.matchdict['id'])
    if protocol_to_delete.delete():
        session.commit()
        return True
    else:
        return False


@view_config(route_name='protocols_delete_change_and_view', request_method='PUT', renderer='json')
def change_protocol_view(request):
    recieved_data = dict(request.POST.items())

    protocol_query = session.query(models.Protocol)
    protocol_to_change = protocol_query.filter_by(protocol_id=recieved_data.get('protocol_id')).first()
    protocol_to_change.protocol_num = recieved_data.get('protocol_num')
    # protocol_to_change.protocol_date = recieved_data.get('protocol_date')
    protocol_to_change.meetings_type_id = recieved_data.get('meetings_type_id')
    protocol_to_change.protocol_name = recieved_data.get('protocol_name')
    protocol_to_change.note = recieved_data.get('note')
    # protocol_to_change.idfilestorage = recieved_data.get('idfilestorage')
    return session.commit()


@view_config(route_name='add_protocol', request_method='GET', renderer='json')
def get_meetings_types_view(request):
    meetings_query = session.query(models.Meeting)
    return [meeting.meetings_type_id for meeting in meetings_query.all()]


@view_config(route_name='add_protocol', request_method='POST', renderer='json')
def add_protocol_view(request):
    recieved_data = dict(request.POST.items())

    protocol_filename = recieved_data.get('protocol_file').filename
    protocol_file = recieved_data.get('protocol_file').file
    protocol_filesize = recieved_data.get('protocol_file').limit

    id_file_storage = str(uuid4())
    new_file = models.Filestorage(idfilestorage=id_file_storage,
                                  filename=protocol_filename,
                                  uri='protocols/download/' + id_file_storage,
                                  filesize=protocol_filesize,
                                  mimeType='text/plain',
                                  description='file description',
                                  authorid=1,
                                  )
    file_path = os.path.join(PROTOCOLS_STORAGE, id_file_storage)
    with open(file_path, 'wb') as output_file:
        shutil.copyfileobj(protocol_file, output_file)

    session.add(new_file)
    session.flush()

    new_protocol = models.Protocol(protocol_num=recieved_data.get('protocol_num'),
                                   protocol_date=recieved_data.get('protocol_date'),
                                   meetings_type_id=recieved_data.get('meetings_type_id'),
                                   protocol_name=recieved_data.get('protocol_name'),
                                   note=recieved_data.get('note'),
                                   idfilestorage=id_file_storage,
                                   )
    session.add(new_protocol)
    session.flush()
    session.commit()
    return new_protocol.protocol_id


@view_config(route_name='download_protocol', request_method='GET')
def download_protocol_view(request):
    protocol_file = f'{PROTOCOLS_STORAGE}/{request.matchdict["uuid"]}'
    if os.path.exists(protocol_file):
        filestorage_query = session.query(models.Filestorage)
        protocol_filename = filestorage_query.\
            filter_by(idfilestorage=request.matchdict["uuid"]).\
            first().filename
        protocol_filename = urllib.request.quote(protocol_filename.encode('utf-8'))

        response = FileResponse(protocol_file)
        response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{protocol_filename}"
        return response
    else:
        return Response(f'Unable to find: {protocol_file}')
