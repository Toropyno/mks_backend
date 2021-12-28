from .model import OrganizationDocument
from .repository import OrganizationDocumentRepository

from mks_backend.entities.documents.construction_document.upload_date_service import UploadDateService
from mks_backend.entities.organizations.organization import OrganizationService


class OrganizationDocumentService:

    def __init__(self):
        self.repo = OrganizationDocumentRepository()
        self.date_service = UploadDateService()
        self.organization_service = OrganizationService()

    def get_organization_document_by_id(self, id_: int) -> OrganizationDocument:
        return self.repo.get_organization_document_by_id(id_)

    def add_organization_document(self, organization_document: OrganizationDocument) -> None:
        self.repo.add_organization_document(organization_document)

    def update_organization_document(self, organization_document: OrganizationDocument) -> None:
        self.repo.update_organization_document(organization_document)

    def delete_organization_document_by_id(self, id_: int) -> None:
        self.repo.delete_organization_document(id_)

    def get_documents_by_organization(self, organization_uuid: str) -> list:
        return self.organization_service.get_by_id(organization_uuid).organization_documents

    def to_mapped_object(self, schema_dict: dict) -> OrganizationDocument:
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
