from pyramid.view import view_config
from pyramid.request import Request

from mks_backend.controllers.schemas.organization_document import OrganizationDocumentSchema
from mks_backend.serializers.documents.organization_document import OrganizationDocumentSerializer
from mks_backend.services.documents.organization_document import OrganizationDocumentService

from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.services.documents.upload_date_utils import set_upload_date


class OrganizationDocumentController:

    def __init__(self, request: Request):
        self.request = request
        self.serializer = OrganizationDocumentSerializer()
        self.service = OrganizationDocumentService()
        self.schema = OrganizationDocumentSchema()

    @view_config(route_name='get_all_organization_documents', renderer='json')
    def get_all_organization_documents(self):
        organization_documents = self.service.get_all_organization_documents()
        return self.serializer.convert_list_to_json(organization_documents)

    @view_config(route_name='get_organization_document', renderer='json')
    def get_organization_document(self):
        id = int(self.request.matchdict['id'])
        organization_document = self.service.get_organization_document_by_id(id)
        return self.serializer.convert_object_to_json(organization_document)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_organization_document', renderer='json')
    def add_organization_document(self):
        organization_document_deserialized = self.schema.deserialize(self.request.json_body)
        organization_document = self.service.convert_schema_to_object(organization_document_deserialized)

        self.service.add_organization_document(organization_document)
        return {'id': organization_document.organization_documents_id}

    @view_config(route_name='delete_organization_document', renderer='json')
    def delete_organization_document(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_organization_document_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_organization_document', renderer='json')
    def edit_organization_document(self):
        id = int(self.request.matchdict['id'])
        organization_document_deserialized = self.schema.deserialize(self.request.json_body)

        old_organization_document = self.service.get_organization_document_by_id(id)

        organization_document_deserialized['id'] = id
        set_upload_date(organization_document_deserialized, old_organization_document)

        organization_document = self.service.convert_schema_to_object(
            organization_document_deserialized,
            old_organization_document.idfilestorage
        )

        self.service.update_organization_document(organization_document)
        return {'id': id}
