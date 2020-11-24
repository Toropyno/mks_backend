from mks_backend.models.documents.doc_type import DocType
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class DocTypeRepository:

    def __init__(self):
        self._query = DBSession.query(DocType)

    def get_all_doc_types(self) -> list:
        return self._query.order_by(DocType.fullname).all()

    @db_error_handler
    def add_doc_type(self, doc_type: DocType) -> None:
        DBSession.add(doc_type)
        DBSession.commit()

    def get_doc_type_by_id(self, id: int) -> DocType:
        return self._query.get(id)

    @db_error_handler
    def update_doc_type(self, doc_type: DocType) -> None:
        DBSession.merge(doc_type)
        DBSession.commit()

    def delete_doc_type_by_id(self, id: int) -> None:
        self._query.filter_by(doctypes_id=id).delete()
        DBSession.commit()
