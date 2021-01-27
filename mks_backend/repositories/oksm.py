from typing import List

from mks_backend.models.oksm import OKSM
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError


class OKSMRepository:

    def __init__(self):
        self._query = DBSession.query(OKSM)

    def get_all_oksms(self) -> List[OKSM]:
        return self._query.order_by(OKSM.shortname).all()

    def add_oksm(self, oksm: OKSM) -> None:
        DBSession.add(oksm)
        DBSession.commit()

    def delete_oksm_by_id(self, id: int) -> None:
        self._query.filter(OKSM.oksm_id == id).delete()
        DBSession.commit()

    def update_oksm(self, new_oksm: OKSM) -> None:
        if DBSession.merge(new_oksm) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('oksm_ad')

    def get_oksm_by_id(self, id_: int) -> OKSM:
        return self._query.get(id_)
