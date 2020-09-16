from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request

from mks_backend.errors.filestorage_error import FilestorageError
from mks_backend.services.filestorage import FilestorageService


class FilestorageController:

    def __init__(self, request: Request):
        self.request = request
        self.service = FilestorageService()

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
