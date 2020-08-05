from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.repositories.filestorage_repository import FilestorageRepository
from mks_backend.services.filestorage_service import FilestorageService
from mks_backend.serializers.filestorage_serializer import FilestorageSerializer


class FilestorageController(object):
    def __init__(self, request):
        self.request = request
        self.repository = FilestorageRepository()
        self.serializer = FilestorageSerializer()
        self.service = FilestorageService()

    @view_config(route_name='upload_file', request_method='POST', renderer='json')
    def upload_file(self):
        try:
            filestorage_id = self.service.create_filestorage_from_request(self.request.POST)
            return {'idFileStorage': str(filestorage_id)}
        except (ValueError, OSError) as error:
            return Response(status=403, json_body={'idFileStorage': str(error)})

    @view_config(route_name='download_file', request_method='GET')
    def download_file(self):
        uuid = self.request.matchdict['uuid']
        response = self.service.get_file(uuid)
        return response
