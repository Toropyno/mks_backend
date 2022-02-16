from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import LitigationDocumentSchema
from .serializer import LitigationDocumentSerializer
from .service import LitigationDocumentService


@view_defaults(renderer='json')
class LitigationDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = LitigationDocumentSerializer()
        self.service = LitigationDocumentService()
        self.schema = LitigationDocumentSchema()

    @view_config(route_name='get_litigation_document')
    def get_litigation_document(self):
        id_ = int(self.request.matchdict['id'])
        litigation_document = self.service.get_litigation_document_by_id(id_)
        return self.serializer.to_json(litigation_document)

    @view_config(route_name='add_litigation_document')
    def add_litigation_document(self):
        litigation_document_deserialized = self.schema.deserialize(self.request.json_body)
        litigation_document = self.serializer.to_mapped_object(litigation_document_deserialized)

        self.service.add_litigation_document(litigation_document)
        return HTTPCreated(json_body={'id': litigation_document.litigation_documents_id})

    @view_config(route_name='edit_litigation_document')
    def edit_litigation_document(self):
        id_ = int(self.request.matchdict['id'])
        litigation_document_deserialized = self.schema.deserialize(self.request.json_body)
        litigation_document_deserialized['id'] = id_

        litigation_document = self.serializer.to_mapped_object(litigation_document_deserialized)
        self.service.update_litigation_document(litigation_document)
        return {'id': id_}

    @view_config(route_name='delete_litigation_document')
    def delete_litigation_document(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_litigation_document_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='get_litigation_documents_by_litigation')
    def get_litigation_documents_by_litigation(self):
        litigation_id = int(self.request.matchdict['id'])
        litigation_documents = self.service.get_litigation_documents_by_litigation(litigation_id)
        return self.serializer.convert_list_to_json(litigation_documents)
