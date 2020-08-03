import urllib
import os

from pyramid.response import FileResponse, Response
from pyramid.view import view_config

from mks_backend.repositories.filestorage_repository import FilestorageRepository
from mks_backend.services.filestorage_service import FilestorageService
from mks_backend.serializers.filestorage_serializer import FilestorageSerializer


PROTOCOLS_STORAGE = '/tmp/protocols'


class FilestorageController(object):
    def __init__(self, request):
        self.request = request
        self.repository = FilestorageRepository()
        self.serializer = FilestorageSerializer()
        self.service = FilestorageService()

    @view_config(route_name='upload_file', request_method='POST', renderer='json')
    def upload_file(self):
        filestorage = self.service.get_filestorage_from_request(self.request.POST.items())
        return {'idFileStorage': str(filestorage.idfilestorage)}

    @view_config(route_name='download_file', request_method='GET')
    def download_file(self):
        uuid = self.request.matchdict['uuid']
        protocol_file = f'{PROTOCOLS_STORAGE}/{uuid}'
        if os.path.exists(protocol_file):
            file = self.repository.get_filestorage_by_id(uuid)
            protocol_filename = file.filename
            protocol_filename = urllib.request.quote(protocol_filename.encode('utf-8'))

            response = FileResponse(protocol_file)
            response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{protocol_filename}"
            return response
        else:
            return Response(f'Unable to find: {protocol_file}')
