from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.repositories.filestorage_hdd import FilestorageException
from mks_backend.services.filestorage_service import FilestorageService


class FilestorageController:
    def __init__(self, request):
        self.request = request
        self.service = FilestorageService()

    @view_config(route_name='upload_file', request_method='POST', renderer='json')
    def upload_file(self):
        try:
            filestorage_id = self.service.create_filestorage(self.request.POST)
            return {'idFileStorage': str(filestorage_id)}
        except FilestorageException as error:
            return Response(status=403,
                            json_body={
                                'error_code': error.code,
                                'text': error.msg,
                            }
                            )

    @view_config(route_name='download_file', request_method='GET')
    def download_file(self):
        uuid = self.request.matchdict['uuid']
        try:
            response = self.service.get_file(uuid)
            return response
        except FilestorageException as error:
            return Response(status=403,
                            json_body={
                                'error_code': error.code,
                                'text': error.msg,
                            }
                            )
