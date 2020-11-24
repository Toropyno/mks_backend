from mks_backend.models.oksm import OKSM
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class OKSMRepository:

    def __init__(self):
        self._query = DBSession.query(OKSM)

    def get_all_oksms(self) -> list:
        return self._query.order_by(OKSM.code).all()

    @db_error_handler
    def add_oksm(self, oksm: OKSM) -> None:
        DBSession.add(oksm)
        DBSession.commit()

    def delete_oksm_by_id(self, id: int) -> None:
        self._query.filter(OKSM.oksm_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_oksm(self, new_oksm: OKSM) -> None:
        DBSession.merge(new_oksm)
        DBSession.commit()

    def get_oksm_by_id(self, id: int) -> OKSM:
        return self._query.get(id)
