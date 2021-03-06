from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import DocType


class DocTypeRepository:

    def __init__(self):
        self._query = DBSession.query(DocType)

    def get_all_doc_types(self) -> list:
        return self._query.order_by(DocType.fullname).all()

    def add_doc_type(self, doc_type: DocType) -> None:
        DBSession.add(doc_type)
        DBSession.commit()

    def get_doc_type_by_id(self, id_: int) -> DocType:
        return self._query.get(id_)

    def update_doc_type(self, doc_type: DocType) -> None:
        if DBSession.merge(doc_type) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('doc_type_ad')

    def delete_doc_type_by_id(self, id_: int) -> None:
        self._query.filter_by(doctypes_id=id_).delete()
        DBSession.commit()
