from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.session import DBSession

from mks_backend.errors.db_basic_error import DBBasicError


class ConstructionDocumentRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionDocument)

    def get_construction_document_by_id(self, id_: int) -> ConstructionDocument:
        construction_document = self._query.get(id_)
        if not construction_document:
            raise DBBasicError('construction_document_nf')
        return construction_document

    def get_many_construction_documents_by_id(self, ids: list) -> list:
        return self._query.filter(
            ConstructionDocument.construction_documents_id.in_(ids)
        ).all()

    def add_construction_document(self, construction_document: ConstructionDocument) -> None:
        DBSession.add(construction_document)
        DBSession.commit()

    def delete_construction_document(self, id_: int) -> None:
        construction_document = self.get_construction_document_by_id(id_)
        DBSession.delete(construction_document)
        DBSession.commit()

    def update_construction_document(self, construction_document: ConstructionDocument) -> None:
        self._query.filter_by(
            construction_documents_id=construction_document.construction_documents_id).update(
            {
                'construction_id': construction_document.construction_id,
                'doctypes_id': construction_document.doctypes_id,
                'doc_number': construction_document.doc_number,
                'doc_date': construction_document.doc_date,
                'doc_name': construction_document.doc_name,
                'note': construction_document.note,
                'idfilestorage': construction_document.idfilestorage,
                'upload_date': construction_document.upload_date,
            }
        )
        DBSession.commit()

    def get_construction_documents_by_construction(self, construction_id: int) -> list:
        return self._query.filter_by(construction_id=construction_id).order_by(
            ConstructionDocument.doc_date
        ).all()
