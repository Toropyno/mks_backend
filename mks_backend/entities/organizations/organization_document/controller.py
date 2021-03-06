from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import OrganizationDocumentSchema
from .serializer import OrganizationDocumentSerializer
from .service import OrganizationDocumentService


@view_defaults(renderer='json')
class OrganizationDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = OrganizationDocumentSchema()
        self.service = OrganizationDocumentService()
        self.serializer = OrganizationDocumentSerializer()

    @view_config(route_name='add_organization_document')
    def add_organization_document(self):
        organization_document_deserialized = self.schema.deserialize(self.request.json_body)
        organization_document = self.service.to_mapped_object(organization_document_deserialized)

        self.service.add_organization_document(organization_document)
        return HTTPCreated(json_body={'id': organization_document.organization_documents_id})

    @view_config(route_name='edit_organization_document')
    def edit_organization_document(self):
        id_ = int(self.request.matchdict.get('id'))
        organization_document_deserialized = self.schema.deserialize(self.request.json_body)
        organization_document_deserialized['id'] = id_

        organization_document = self.service.to_mapped_object(organization_document_deserialized)
        self.service.update_organization_document(organization_document)
        return {'id': id_}

    @view_config(route_name='delete_organization_document')
    def delete_organization_document(self):
        id_ = int(self.request.matchdict.get('id'))
        self.service.delete_organization_document_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='get_documents_by_organization')
    def get_documents_by_organization(self):
        organization_id = self.request.matchdict.get('organization_uuid')
        documents = self.service.get_documents_by_organization(organization_id)
        return self.serializer.convert_list_to_json(documents)

    @view_config(route_name='get_document_by_organization')
    def get_document_by_organization(self):
        document_id = self.request.matchdict.get('id')
        document = self.service.get_organization_document_by_id(document_id)
        return self.serializer.to_json(document)
