from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ObjectFileSchema
from .serializer import ObjectFileSerializer
from .service import ObjectFileService


@view_defaults(renderer='json')
class ObjectFileController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectFileService()
        self.serializer = ObjectFileSerializer()
        self.schema = ObjectFileSchema()

    @view_config(route_name='get_all_object_files')
    def get_all_object_files(self):
        object_files = self.service.get_all_object_files()
        return self.serializer.convert_list_to_json(object_files)

    @view_config(route_name='add_object_file')
    def add_object_file(self):
        object_file_deserialized = self.schema.deserialize(self.request.json_body)

        self.service.set_upload_date(object_file_deserialized)
        object_file = self.serializer.convert_schema_to_object(object_file_deserialized)

        self.service.add_object_file(object_file)
        return {'id': object_file.object_files_id}

    @view_config(route_name='delete_object_file')
    def delete_object_file(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_object_file_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_object_file')
    def edit_object_file(self):
        id = int(self.request.matchdict['id'])
        object_file_deserialized = self.schema.deserialize(self.request.json_body)

        object_file_deserialized['id'] = id
        self.service.set_upload_date(object_file_deserialized)
        new_object_file = self.serializer.convert_schema_to_object(object_file_deserialized)

        self.service.update_object_file(new_object_file)
        return {'id': new_object_file.object_files_id}

    @view_config(route_name='get_object_file')
    def get_object_file(self):
        id = int(self.request.matchdict['id'])
        object_file = self.service.get_object_file_by_id(id)
        return self.serializer.convert_object_to_json(object_file)

    @view_config(route_name='get_object_files_by_object')
    def get_object_files_by_object(self):
        object_id = int(self.request.matchdict['id'])
        object_files = self.service.get_object_files_by_object(object_id)
        return self.serializer.convert_list_to_json(object_files)