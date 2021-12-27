from pyramid.view import view_config, view_defaults
from pyramid.request import Request

from .schema import DocTypeSchema
from .serializer import DocTypeSerializer
from .service import DocTypeService


@view_defaults(renderer='json')
class DocTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = DocTypeSerializer()
        self.service = DocTypeService()
        self.schema = DocTypeSchema()

    @view_config(route_name='get_all_doc_types')
    def get_all_doc_types(self):
        doc_types = self.service.get_all_doc_types()
        return self.serializer.convert_list_to_json(doc_types)

    @view_config(route_name='add_doc_type')
    def add_doc_type(self):
        doc_type_deserialized = self.schema.deserialize(self.request.json_body)

        doc_type = self.serializer.to_mapped_object(doc_type_deserialized)
        self.service.add_doc_type(doc_type)
        return {'id': doc_type.doctypes_id}

    @view_config(route_name='get_doc_type')
    def get_doc_type(self):
        id = int(self.request.matchdict['id'])
        doc_type = self.service.get_doc_type_by_id(id)
        return self.serializer.to_json(doc_type)

    @view_config(route_name='delete_doc_type')
    def delete_doc_type(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_doc_type_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_doc_type')
    def edit_doc_type(self):
        id = int(self.request.matchdict['id'])
        doc_type_deserialized = self.schema.deserialize(self.request.json_body)

        doc_type_deserialized['id'] = id
        doc_type = self.serializer.to_mapped_object(doc_type_deserialized)

        self.service.update_doc_type(doc_type)
        return {'id': id}
