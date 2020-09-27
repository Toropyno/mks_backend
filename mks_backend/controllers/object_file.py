from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.controllers.schemas.object_file import ObjectFileSchema
from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.serializers.object_file import ObjectFileSerializer
from mks_backend.services.object_file import ObjectFileService


class ObjectFileController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ObjectFileSerializer()
        self.service = ObjectFileService()
        self.schema = ObjectFileSchema()

    @view_config(route_name='get_all_object_files', renderer='json')
    def get_all_object_files(self):
        object_files = self.service.get_all_object_files()
        return self.serializer.convert_list_to_json(object_files)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_object_file', renderer='json')
    def add_object_file(self):
        object_file_deserialized = self.schema.deserialize(self.request.json_body)
        object_file = self.serializer.convert_schema_to_object(object_file_deserialized)
        self.service.add_object_file(object_file)
        return {'id': object_file.object_file_id}

    @view_config(route_name='get_object_file', renderer='json')
    def get_object_file(self):
        object_file = self.service.get_object_file_by_id(self.get_ID_from_request())
        return self.serializer.convert_object_to_json(object_file)

    @view_config(route_name='delete_object_file', renderer='json')
    def delete_object_file(self):
        id = self.get_ID_from_request()
        self.service.delete_object_file_by_id(id)
        return {'id': id}

    def get_ID_from_request(self) -> int:
        return int(self.request.matchdict['id'])
