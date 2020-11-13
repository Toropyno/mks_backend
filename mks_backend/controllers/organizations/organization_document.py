from pyramid.view import view_config, view_defaults
from pyramid.request import Request

from mks_backend.controllers.schemas.organizations.organization_document import OrganizationDocumentSchema
from mks_backend.serializers.organizations.organization_document import OrganizationDocumentSerializer
from mks_backend.services.organizations.organization_document import OrganizationDocumentService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error


@view_defaults(renderer='json')
class OrganizationDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = OrganizationDocumentSchema()
        self.service = OrganizationDocumentService()
        self.serializer = OrganizationDocumentSerializer()

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_organization_document')
    def add_organization_document(self):
        organization_document_deserialized = self.schema.deserialize(self.request.json_body)
        organization_document = self.service.convert_schema_to_object(organization_document_deserialized)

        self.service.add_organization_document(organization_document)
        return {'id': organization_document.organization_documents_id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_organization_document')
    def edit_organization_document(self):
        id = int(self.request.matchdict['id'])
        organization_document_deserialized = self.schema.deserialize(self.request.json_body)
        organization_document_deserialized['id'] = id

        organization_document = self.service.convert_schema_to_object(organization_document_deserialized)
        self.service.update_organization_document(organization_document)
        return {'id': id}

    @view_config(route_name='delete_organization_document')
    def delete_organization_document(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_organization_document_by_id(id)
        return {'id': id}

    @handle_db_error
    @view_config(route_name='get_documents_by_organization')
    def get_documents_by_organization(self):
        organization_id = self.request.matchdict.get('organization_uuid')
        documents = self.service.get_documents_by_organization(organization_id)
        return self.serializer.convert_list_to_json(documents)
