from .model import Courts
from mks_backend.session import DBSession


from mks_backend.errors import DBBasicError


class CourtsRepository:

    def __init__(self):
        self._query = DBSession.query(Courts)

    def get_all_courts(self) -> list:
        return self._query.order_by(Courts.fullname).all()

    def add_court(self, construction_court: Courts) -> None:
        DBSession.add(construction_court)
        DBSession.commit()

    def delete_court_by_id(self, id_: int) -> None:
        self._query.filter(Courts.courts_id == id_).delete()
        DBSession.commit()

    def update_court(self, new_court: Courts) -> None:
        if DBSession.merge(new_court) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('court_ad')

    def get_court_by_id(self, id: int):
        court = self._query.get(id)
        if not court:
            raise DBBasicError('court_nf')
        return court
