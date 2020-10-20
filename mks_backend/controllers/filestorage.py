from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.filestorage import FileStorageSerializer
from mks_backend.services.filestorage import FilestorageService

from mks_backend.errors.handle_controller_error import handle_filestorage_error


class FilestorageController:

    def __init__(self, request: Request):
        self.request = request
        self.service = FilestorageService()
        self.serializer = FileStorageSerializer()

    @handle_filestorage_error
    @view_config(route_name='upload_file', renderer='json')
    def upload_file(self):
        filestorage_id = self.service.create_filestorage(self.request.POST)
        return {'idFileStorage': str(filestorage_id)}

    @handle_filestorage_error
    @view_config(route_name='download_file')
    def download_file(self):
        uuid = self.request.matchdict['uuid']
        response = self.service.get_file(uuid)
        return response

    @handle_filestorage_error
    @view_config(route_name='get_file_info', renderer='json')
    def get_file_info(self):
        uuid = self.request.params.get('idFileStorage')
        filestorage = self.service.get_filestorage_by_id(uuid)
        return self.serializer.to_json(filestorage)

    @view_config(route_name='get_filestorages_by_object', renderer='json')
    def get_filestorages_by_object(self):
        object_id = int(self.request.matchdict['id'])
        filestorages = self.service.get_filestorages_by_object(object_id)
        return self.serializer.convert_list_to_json(filestorages)
