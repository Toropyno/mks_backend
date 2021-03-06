from mks_backend.session import DBSession

from .model import OrganizationDocument


class OrganizationDocumentRepository:

    def __init__(self):
        self._query = DBSession.query(OrganizationDocument)

    def get_organization_document_by_id(self, id_: int) -> OrganizationDocument:
        return self._query.get(id_)

    def add_organization_document(self, organization_document: OrganizationDocument) -> None:
        DBSession.add(organization_document)
        DBSession.commit()

    def delete_organization_document(self, id_: int) -> None:
        self._query.filter_by(organization_documents_id=id_).delete()
        DBSession.commit()

    def update_organization_document(self, organization_document: OrganizationDocument) -> None:
        self._query.filter_by(
            organization_documents_id=organization_document.organization_documents_id).update(
            {
                'doc_name': organization_document.doc_name,
                'note': organization_document.note,
                'upload_date': organization_document.upload_date,
                'doc_date': organization_document.doc_date,
                'doc_number': organization_document.doc_number,
                'organizations_id': organization_document.organizations_id,
                'doctypes_id': organization_document.doctypes_id,
                'idfilestorage': organization_document.idfilestorage,
            }
        )
        DBSession.commit()
