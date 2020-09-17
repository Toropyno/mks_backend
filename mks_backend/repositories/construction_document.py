from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.construction_document import ConstructionDocument
from mks_backend.repositories import DBSession
from mks_backend.repositories.filestorage import FilestorageRepository


class ConstructionDocumentRepository:

    def get_construction_document_by_id(self, id: int) -> ConstructionDocument:
        return DBSession.query(ConstructionDocument).get(id)

    def get_all_construction_documents(self) -> list:
        return DBSession.query(ConstructionDocument).all()

    @db_error_handler
    def add_construction_document(self, construction_document: ConstructionDocument) -> None:
        DBSession.add(construction_document)
        DBSession.commit()

    def delete_construction_document_by_id_with_filestorage_cascade(self, id: int) -> None:
        construction_document = self.get_construction_document_by_id(id)
        file_storage_id = construction_document.idfilestorage
        DBSession.delete(construction_document)
        DBSession.commit()
        FilestorageRepository.delete_filestorage_by_id(file_storage_id)

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

    def get_many_construction_documents_by_id(self, ids: list) -> list:
        return DBSession.query(ConstructionDocument).filter(
            ConstructionDocument.construction_documents_id.in_(ids)).all()
