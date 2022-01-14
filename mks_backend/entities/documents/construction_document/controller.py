from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ConstructionDocumentSchema
from .serializer import ConstructionDocumentSerializer
from .service import ConstructionDocumentService


@view_defaults(renderer='json')
class ConstructionDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = ConstructionDocumentSerializer()
        self.service = ConstructionDocumentService()
        self.schema = ConstructionDocumentSchema()

    @view_config(route_name='get_construction_document')
    def get_construction_document(self):
        id_ = int(self.request.matchdict['id'])
        construction_document = self.service.get_construction_document_by_id(id_)
        return self.serializer.to_json(construction_document)

    @view_config(route_name='add_construction_document')
    def add_construction_document(self):
        construction_document_deserialized = self.schema.deserialize(self.request.json_body)
        construction_document = self.service.to_mapped_object(construction_document_deserialized)

        self.service.add_construction_document(construction_document)
        return HTTPCreated(json_body={'id': construction_document.construction_documents_id})

    @view_config(route_name='edit_construction_document')
    def edit_construction_document(self):
        id_ = int(self.request.matchdict['id'])
        construction_document_deserialized = self.schema.deserialize(self.request.json_body)
        construction_document_deserialized['id'] = id_

        construction_document = self.service.to_mapped_object(construction_document_deserialized)
        self.service.update_construction_document(construction_document)
        return {'id': id_}

    @view_config(route_name='delete_construction_document')
    def delete_construction_document(self):
        id_ = int(self.request.matchdict['id'])
        self.service.delete_construction_document_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='get_construction_documents_by_construction')
    def get_construction_documents_by_construction(self):
        construction_id = int(self.request.matchdict['id'])
        construction_documents = self.service.get_construction_documents_by_construction(construction_id)
        return self.serializer.convert_list_to_json(construction_documents)
