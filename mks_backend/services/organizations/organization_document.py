from mks_backend.models.organizations.organization_document import OrganizationDocument
from mks_backend.repositories.organizations.organization_document import OrganizationDocumentRepository
from mks_backend.services.documents.upload_date import UploadDateService
from mks_backend.services.organizations.organization import OrganisationService


class OrganizationDocumentService:

    def __init__(self):
        self.repo = OrganizationDocumentRepository()
        self.date_service = UploadDateService()
        self.organization_service = OrganisationService()

    def get_organization_document_by_id(self, id: int) -> OrganizationDocument:
        return self.repo.get_organization_document_by_id(id)

    def add_organization_document(self, organization_document: OrganizationDocument) -> None:
        self.repo.add_organization_document(organization_document)

    def update_organization_document(self, organization_document: OrganizationDocument) -> None:
        self.repo.update_organization_document(organization_document)

    def delete_organization_document_by_id(self, id: int) -> None:
        self.repo.delete_organization_document(id)

    def get_documents_by_organization(self, organization_uuid: str) -> list:
        return self.organization_service.get_by_id(organization_uuid).organization_documents

    def convert_schema_to_object(self, schema_dict: dict) -> OrganizationDocument:
        organization_document = OrganizationDocument()

        organization_document.idfilestorage = schema_dict.get('idFileStorage')
        self.date_service.set_upload_date_by_idfilestorage(organization_document)

        organization_document.organization_documents_id = schema_dict.get('id')
        organization_document.doc_name = schema_dict.get('docName')
        organization_document.note = schema_dict.get('note')
        organization_document.doc_date = schema_dict.get('docDate')
        organization_document.doc_number = schema_dict.get('docNumber')
        organization_document.organizations_id = schema_dict.get('organizationId')
        organization_document.doctypes_id = schema_dict.get('docTypeId')

        return organization_document
