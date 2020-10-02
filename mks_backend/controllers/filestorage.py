from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.serializers.filestorage import FileStorageSerializer
from mks_backend.services.filestorage import FilestorageService

from mks_backend.errors.filestorage_error import FilestorageError


class FilestorageController:

    def __init__(self, request: Request):
        self.request = request
        self.service = FilestorageService()
        self.serializer = FileStorageSerializer()

    @view_config(route_name='upload_file', renderer='json')
    def upload_file(self):
        try:
            filestorage_id = self.service.create_filestorage(self.request.POST)
            return {'idFileStorage': str(filestorage_id)}
        except FilestorageError as error:
            return Response(
                status=403,
                json_body={
                    'error_code': error.code,
                    'text': error.msg,
                }
            )

    @view_config(route_name='download_file')
    def download_file(self):
        uuid = self.request.matchdict['uuid']
        try:
            response = self.service.get_file(uuid)
            return response
        except FilestorageError as error:
            return Response(
                status=403,
                json_body={
                    'error_code': error.code,
                    'text': error.msg,
                }
            )

    @view_config(route_name='get_file_info', renderer='json')
    def get_file_info(self):
        uuid = self.request.params.get('idFileStorage')
        try:
            return self.service.get_file_info(uuid)
        except FilestorageError as error:
            return Response(
                status=403,
                json_body={
                    'error_code': error.code,
                    'text': error.msg,
                }
            )

    @view_config(route_name='get_filestorages_by_object', renderer='json')
    def get_filestorages_by_object(self):
        object_id = int(self.request.matchdict['id'])
        filestorages = self.service.get_filestorages_by_object(object_id)
        file_storages = self.get_file_storages(filestorages)
        return file_storages

    def get_file_storages(self, filestorages):
        file_storages = []
        for file_st in filestorages:
            file_info = None
            if file_st.idfilestorage:
                file_info = self.service.get_file_info(str(file_st.idfilestorage))
            file_storages.append(self.serializer.convert_object_to_json(file_st, file_info))
        return file_storages
