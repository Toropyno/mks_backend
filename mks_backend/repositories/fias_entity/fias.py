from mks_backend.models.fias import FIAS
from mks_backend.repositories import DBSession


class FIASRepository:

    def add_fias(self, fias: FIAS) -> None:
        DBSession.add(fias)
        DBSession.commit()

    def get_fias_by_id(self, id: int) -> FIAS:
        return DBSession.query(FIAS).get(id)

    def delete_fias_by_id(self, id: int) -> None:
        DBSession.delete(self.get_fias_by_id(id))
        DBSession.commit()

    def get_fias_by_aoid(self, aoid: str) -> FIAS:
        return DBSession.query(FIAS).filter(FIAS.aoid == aoid).first()
