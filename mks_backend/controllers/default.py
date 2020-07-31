import os
import urllib
from uuid import uuid4
from shutil import copyfileobj

from pyramid.view import view_config
from pyramid.response import FileResponse, Response

from mks_backend.models import models
from mks_backend.models import DBSession

PROTOCOLS_STORAGE = '/tmp/protocols'


@view_config(route_name='protocols', request_method='GET', renderer='json')
def get_all_protocols(request):
    if request.params:
        params = dict(request.params)
        protocols = DBSession.query(models.Protocol)
        filter_dict = dict(zip(params.keys(), params.values()))
        return protocols.filter_by(**filter_dict).all()
    else:
        protocols = DBSession.query(models.Protocol).all()
        return protocols


@view_config(route_name='protocols_delete_change_and_view', request_method='GET', renderer='json')
def get_protocol(request):
    protocols_query = DBSession.query(models.Protocol)
    protocol_to_view = protocols_query.filter_by(protocol_id=request.matchdict['id']).first()
    if protocol_to_view is None:
        return False
    else:
        return protocol_to_view


@view_config(route_name='protocols_delete_change_and_view', request_method='DELETE', renderer='json')
def delete_protocol(request):
    protocol_query = DBSession.query(models.Protocol)
    filestorage_query = DBSession.query(models.Filestorage)

    protocol_to_delete = protocol_query.filter_by(protocol_id=request.matchdict['id']).one()
    filestorage_to_delete = filestorage_query.filter_by(idfilestorage=protocol_to_delete.idfilestorage).one()

    path_to_file = PROTOCOLS_STORAGE + '/' + str(filestorage_to_delete.idfilestorage)
    if os.path.exists(path_to_file):
        os.remove(path_to_file)
        DBSession.delete(filestorage_to_delete)
        DBSession.commit()
        return True
    else:
        return False


@view_config(route_name='protocols_delete_change_and_view', request_method='PUT', renderer='json')
def change_protocol(request):
    received_data = request.json_body

    protocol_query = DBSession.query(models.Protocol)
    protocol_to_change = protocol_query.filter_by(protocol_id=received_data.get('protocolId')).first()

    protocol_to_change.protocol_num = received_data.get('protocolNumber')
    protocol_to_change.protocol_date = received_data.get('protocolDate')
    protocol_to_change.meetings_type_id = received_data.get('meetingsTypeId')
    protocol_to_change.protocol_name = received_data.get('protocolName')
    protocol_to_change.note = received_data.get('note')
    return DBSession.commit()


@view_config(route_name='add_protocol', request_method='GET', renderer='json')
def get_meetings_types(request):
    meetings_query = DBSession.query(models.Meeting)
    return [meeting.meetings_type_id for meeting in meetings_query.all()]


@view_config(route_name='add_protocol', request_method='POST', renderer='json')
def add_protocol(request):
    received_data = request.json_body

    new_protocol = models.Protocol(protocol_num=received_data.get('protocolNumber'),
                                   protocol_date=received_data.get('protocolDate'),
                                   meetings_type_id=received_data.get('meetingsTypeId'),
                                   protocol_name=received_data.get('protocolName'),
                                   note=received_data.get('note'),
                                   idfilestorage=received_data.get('idFileStorage'),
                                   )
    DBSession.add(new_protocol)
    DBSession.commit()
    return new_protocol.protocol_id


@view_config(route_name='download_file', request_method='GET')
def download_file(request):
    protocol_file = f'{PROTOCOLS_STORAGE}/{request.matchdict["uuid"]}'
    if os.path.exists(protocol_file):
        filestorage_query = DBSession.query(models.Filestorage)
        protocol_filename = filestorage_query. \
            filter_by(idfilestorage=request.matchdict["uuid"]). \
            first().filename
        protocol_filename = urllib.request.quote(protocol_filename.encode('utf-8'))

        response = FileResponse(protocol_file)
        response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{protocol_filename}"
        return response
    else:
        return Response(f'Unable to find: {protocol_file}')


@view_config(route_name='upload_file', request_method='POST', renderer='json')
def upload_file(request):
    received_data = dict(request.POST.items())

    protocol_filename = received_data.get('protocolFile').filename
    protocol_file = received_data.get('protocolFile').file
    protocol_filesize = received_data.get('protocolFile').limit

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
        copyfileobj(protocol_file, output_file)

    DBSession.add(new_file)
    DBSession.commit()

    return {'idFileStorage': id_file_storage}
