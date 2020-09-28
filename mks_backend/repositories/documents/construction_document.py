from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.repositories import DBSession


class ConstructionDocumentRepository:

    def get_construction_document_by_id(self, id: int) -> ConstructionDocument:
        return DBSession.query(ConstructionDocument).get(id)

    def get_all_construction_documents(self) -> list:
        return DBSession.query(ConstructionDocument).all()

    def get_many_construction_documents_by_id(self, ids: list) -> list:
        return DBSession.query(ConstructionDocument).filter(
            ConstructionDocument.construction_documents_id.in_(ids)
        ).all()

    @db_error_handler
    def add_construction_document(self, construction_document: ConstructionDocument) -> None:
        DBSession.add(construction_document)
        DBSession.commit()

    def delete_construction_document(self, construction_document: ConstructionDocument) -> None:
        DBSession.delete(construction_document)
        DBSession.commit()

    @db_error_handler
    def update_construction_document(self, construction_document: ConstructionDocument) -> None:
        DBSession.query(ConstructionDocument).filter_by(
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
        return DBSession.query(ConstructionDocument).filter_by(construction_id=construction_id).all()
