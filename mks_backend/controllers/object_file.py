from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.object_file import ObjectFileSerializer
from mks_backend.services.object_file import ObjectFileService


class ObjectFileController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ObjectFileSerializer()
        self.service = ObjectFileService()

    @view_config(route_name='get_all_object_files', renderer='json')
    def get_fields_all_object_files(self):
        object_files = self.service.get_fields_all_object_files()
        return self.serializer.convert_list_to_json(object_files)
