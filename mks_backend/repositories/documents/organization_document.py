from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.documents.organization_document import OrganizationDocument
from mks_backend.repositories import DBSession


class OrganizationDocumentRepository:

    def get_organization_document_by_id(self, id: int) -> OrganizationDocument:
        return DBSession.query(OrganizationDocument).get(id)

    def get_all_organization_documents(self) -> list:
        return DBSession.query(OrganizationDocument).order_by(OrganizationDocument.doc_date).all()

    @db_error_handler
    def add_organization_document(self, organization_document: OrganizationDocument) -> None:
        DBSession.add(organization_document)
        DBSession.commit()

    def delete_organization_document(self, organization_document: OrganizationDocument) -> None:
        DBSession.delete(organization_document)
        DBSession.commit()

    @db_error_handler
    def update_organization_document(self, organization_document: OrganizationDocument) -> None:
        DBSession.query(OrganizationDocument).filter_by(
            organization_documents_id=organization_document.organization_documents_id).update(
            {
                'doc_name': organization_document.doc_name,
                'note': organization_document.note,
                'upload_date': organization_document.upload_date,
                'doc_date': organization_document.doc_date,
                'doc_number': organization_document.doc_number,
                'organization': organization_document.organizations_id,
                'doctypes_id': organization_document.doctypes_id,
                'idfilestorage': organization_document.idfilestorage,
            }
        )
        DBSession.commit()
