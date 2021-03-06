from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import LeadershipPosition


class LeadershipPositionRepository:

    def __init__(self):
        self._query = DBSession.query(LeadershipPosition)

    def get_all_leadership_positions(self) -> list:
        return self._query.all()

    def add_leadership_position(self, leadership_position: LeadershipPosition) -> None:
        DBSession.add(leadership_position)
        DBSession.commit()

    def delete_leadership_position_by_id(self, id_: int) -> None:
        self._query.filter(LeadershipPosition.leadership_positions_id == id_).delete()
        DBSession.commit()

    def update_leadership_position(self, new_leadership_position: LeadershipPosition) -> None:
        if DBSession.merge(new_leadership_position) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('leadership_position_ad')

    def get_leadership_position_by_id(self, id_: int) -> LeadershipPosition:
        return self._query.get(id_)
