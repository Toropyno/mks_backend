from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ObjectDocumentSchema
from .service import ObjectDocumentService

from mks_backend.entities.documents.construction_document import ConstructionDocumentSerializer


@view_defaults(renderer='json')
class ObjectDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectDocumentService()
        self.schema = ObjectDocumentSchema()
        self.document_serializer = ConstructionDocumentSerializer()

    @view_config(route_name='get_construction_documents_by_object')
    def get_construction_documents_by_object(self):
        object_id = int(self.request.matchdict['id'])
        object_documents = self.service.get_documents_by_construction_object(object_id)

        return self.document_serializer.convert_list_to_json(object_documents)

    @view_config(route_name='edit_construction_document_and_object_relations')
    def edit_construction_document_and_object_relations(self):
        object_id = int(self.request.matchdict['id'])
        construction_documents_ids_deserialized = self.schema.deserialize(self.request.json_body)['documents']
        self.service.edit_construction_document_and_object_relations(object_id, construction_documents_ids_deserialized)
        return {'id': object_id}
