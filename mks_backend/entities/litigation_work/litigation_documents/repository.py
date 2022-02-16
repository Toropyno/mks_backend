from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.session import DBSession

from .model import LitigationDocument


class LitigationDocumentRepository:

    def __init__(self):
        self._query = DBSession.query(LitigationDocument)

    def get_litigation_document_by_id(self, id_: int) -> LitigationDocument:
        litigation_document = self._query.get(id_)
        if not litigation_document:
            raise DBBasicError('litigation_document_nf')
        return litigation_document

    def get_many_litigation_documents_by_id(self, ids: list) -> list:
        return self._query.filter(
            LitigationDocument.litigation_documents_id.in_(ids)
        ).all()

    def add_litigation_document(self, litigation_document: LitigationDocument) -> None:
        DBSession.add(litigation_document)
        DBSession.commit()

    def delete_litigation_document(self, id_: int) -> None:
        litigation_document = self.get_litigation_document_by_id(id_)
        DBSession.delete(litigation_document)
        DBSession.commit()

    def update_litigation_document(self, litigation_document: LitigationDocument) -> None:
        self._query.filter_by(
            litigation_documents_id=litigation_document.litigation_documents_id).update(
            {
                'litigation_id': litigation_document.litigation_id,
                'doctypes_id': litigation_document.doctypes_id,
                'doc_number': litigation_document.doc_number,
                'doc_date': litigation_document.doc_date,
                'doc_name': litigation_document.doc_name,
                'note': litigation_document.note,
                'idfilestorage': litigation_document.idfilestorage,
                'upload_date': litigation_document.upload_date,
            }
        )
        DBSession.commit()

    def get_litigation_documents_by_litigation(self, litigation_id: int) -> list:
        return self._query.filter_by(litigation_id=litigation_id).order_by(
            LitigationDocument.doc_date
        ).all()
