from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.documents.doc_type import DocType
from mks_backend.repositories import DBSession


class DocTypeRepository:

    def get_all_doc_types(self) -> list:
        return DBSession.query(DocType).order_by(DocType.fullname).all()

    @db_error_handler
    def add_doc_type(self, doc_type: DocType) -> None:
        DBSession.add(doc_type)
        DBSession.commit()

    def get_doc_type_by_id(self, id: int) -> DocType:
        return DBSession.query(DocType).get(id)

    @db_error_handler
    def update_doc_type(self, doc_type: DocType) -> None:
        DBSession.query(DocType).filter_by(doctypes_id=doc_type.doctypes_id).update(
            {
                'code': doc_type.code,
                'fullname': doc_type.fullname,
            }
        )
        DBSession.commit()

    def delete_doc_type_by_id(self, id: int) -> None:
        doc_type = self.get_doc_type_by_id(id)
        DBSession.delete(doc_type)
        DBSession.commit()
