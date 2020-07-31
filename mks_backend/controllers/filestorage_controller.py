from uuid import uuid4
import urllib
from shutil import copyfileobj
import os

from pyramid.response import FileResponse, Response
from pyramid.view import view_config, view_defaults

from mks_backend.repositories.filestorage_repository import FilestorageRepository
from mks_backend.services.filestorage_service import FilestorageService
from mks_backend.serializers.filestorage_serializer import FilestorageSerializer
from mks_backend.models.filestorage import Filestorage


PROTOCOLS_STORAGE = '/tmp/protocols'


class FilestorageController(object):
    def __init__(self, request):
        self.request = request
        self.repository = FilestorageRepository()
        self.serializer = FilestorageSerializer()
        self.service = FilestorageService()

    @view_config(route_name='upload_file', request_method='POST', renderer='json')
    def upload_file(self):
        filestorage = self.get_filestorage_object_from_request_params()
        self.repository.add_file(filestorage)
        return {'idFileStorage': str(filestorage.idfilestorage)}

    @view_config(route_name='download_file', request_method='GET')
    def download_file(self):
        uuid = self.request.matchdict['uuid']
        protocol_file = f'{PROTOCOLS_STORAGE}/{uuid}'
        if os.path.exists(protocol_file):
            file = self.repository.get_file(uuid)
            protocol_filename = file.filename
            protocol_filename = urllib.request.quote(protocol_filename.encode('utf-8'))

            response = FileResponse(protocol_file)
            response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{protocol_filename}"
            return response
        else:
            return Response(f'Unable to find: {protocol_file}')

    def get_filestorage_object_from_request_params(self):
        file = dict(self.request.POST.items()).get('protocolFile')
        id_file_storage = str(uuid4())

        file_path = os.path.join(PROTOCOLS_STORAGE, id_file_storage)
        with open(file_path, 'wb') as output_file:
            copyfileobj(file.file, output_file)

        return Filestorage(idfilestorage=id_file_storage,
                           filename=file.filename,
                           uri='protocols/download/' + id_file_storage,
                           filesize=file.limit,
                           mimeType='text/plain',
                           description='file description',
                           authorid=1)
