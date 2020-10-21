from pyramid.request import Request
from pyramid.view import view_config
from pyramid.response import FileResponse

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
        file = self.request.POST.get('file')
        filestorage_id = self.service.create_filestorage(file)
        return {'idFileStorage': filestorage_id}

    @handle_filestorage_error
    @view_config(route_name='download_file')
    def download_file(self):
        uuid = self.request.matchdict['uuid']
        filename, path_to_file = self.service.get_file(uuid)

        response = FileResponse(path_to_file)
        response.headers['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(filename)
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
