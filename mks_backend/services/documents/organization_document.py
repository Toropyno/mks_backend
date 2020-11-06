from datetime import datetime

from mks_backend.models.documents.organization_document import OrganizationDocument
from mks_backend.repositories.documents.organization_document import OrganizationDocumentRepository

from mks_backend.services.documents.upload_date_utils import update_idfilestorage_with_upload_date


class OrganizationDocumentService:

    def __init__(self):
        self.repo = OrganizationDocumentRepository()

    def get_all_organization_documents(self) -> list:
        return self.repo.get_all_organization_documents()

    def get_organization_document_by_id(self, id: int) -> OrganizationDocument:
        return self.repo.get_organization_document_by_id(id)

    def add_organization_document(self, organization_document: OrganizationDocument) -> None:
        self.repo.add_organization_document(organization_document)

    def update_organization_document(self, organization_document: OrganizationDocument) -> None:
        self.repo.update_organization_document(organization_document)

    def delete_organization_document_by_id(self, id: int) -> None:
        organization_document = self.get_organization_document_by_id(id)
        self.repo.delete_organization_document(organization_document)

    def convert_schema_to_object(self, schema_dict: dict, old_idfilestorage=None) -> OrganizationDocument:
        organization_document = OrganizationDocument()

        organization_document.idfilestorage = schema_dict.get('idFileStorage')
        organization_document.upload_date = datetime.now()
        if old_idfilestorage:
            organization_document = update_idfilestorage_with_upload_date(organization_document, old_idfilestorage)

        organization_document.organization_documents_id = schema_dict.get('id')
        organization_document.doc_name = schema_dict.get('docName')
        organization_document.note = schema_dict.get('note')
        organization_document.doc_date = schema_dict.get('docDate')
        organization_document.doc_number = schema_dict.get('docNumber')
        organization_document.organizations_id = schema_dict.get('organizationsId')
        organization_document.doctypes_id = schema_dict.get('docTypesId')

        return organization_document
