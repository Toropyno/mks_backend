from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.fias import FIAS
from mks_backend.repositories import DBSession


class FIASRepository:

    @db_error_handler
    def add_fias(self, fias: FIAS) -> None:
        DBSession.add(fias)
        DBSession.commit()

    def get_fias_by_id(self, id: int) -> FIAS:
        return DBSession.query(FIAS).get(id)

    def delete_fias_by_id(self, id: int) -> None:
        DBSession.query(FIAS).filter(FIAS.id == id).delete()
        DBSession.commit()

    def get_fias_by_aoid(self, aoid: str) -> FIAS:
        return DBSession.query(FIAS).filter(FIAS.aoid == aoid).first()
