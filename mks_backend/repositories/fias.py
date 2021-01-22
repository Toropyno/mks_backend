from mks_backend.session import DBSession
from mks_backend.models.fias import FIAS


class FIASrepo:

    def __init__(self):
        self._query = DBSession.query(FIAS)

    def get_fias_by_id(self, id: int) -> FIAS:
        return self._query.get(id)

    def get_fias_by_aoid(self, aoid):
        return self._query.filter(FIAS.aoid == aoid).first()

    def get_all_fiases(self) -> list:
        return self._query.all()

    def add_fias(self, fias: FIAS) -> None:
        DBSession.add(fias)
        DBSession.commit()

    def delete_fias_by_id(self, id: int) -> None:
        fias = self.get_fias_by_id(id)
        DBSession.delete(fias)
        DBSession.commit()
