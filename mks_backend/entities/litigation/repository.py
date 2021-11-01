from sqlalchemy import desc
from .model import Litigation
from mks_backend.session import DBSession
from mks_backend.errors import DBBasicError


class LitigationRepository:
    def __init__(self):
        self._query = DBSession.query(Litigation)

    def get_all_litigations(self) -> list:
        return self._query.order_by(Litigation.litigation_id).all()

    def add_litigation(self, litigation: Litigation) -> None:
        DBSession.add(litigation)
        DBSession.commit()

    def delete_litigation_by_id(self, id: int) -> None:
        self._query.filter(Litigation.litigation_id == id).delete()
        DBSession.commit()

    def update_litigation(self, new_litigation: Litigation) -> None:
        if DBSession.merge(new_litigation) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('litigation_ad')

    def get_litigation_by_id(self, id: int):
        litigation = self._query.filter(
            Litigation.litigation_id == id
        ).order_by(desc(Litigation.litigation_id)).first()
        if not litigation:
            raise DBBasicError('litigation_nf')
        return litigation
