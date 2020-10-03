from mks_backend.models.trips.leadership_position import LeadershipPosition
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class LeadershipPositionRepository:

    def __init__(self):
        self._query = DBSession.query(LeadershipPosition)

    def get_all_leadership_positions(self) -> list:
        return self._query.all()

    @db_error_handler
    def add_leadership_position(self, leadership_position: LeadershipPosition) -> None:
        DBSession.add(leadership_position)
        DBSession.commit()

    def delete_leadership_position_by_id(self, id: int) -> None:
        self._query.filter(LeadershipPosition.leadership_positions_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_leadership_position(self, new_leadership_position: LeadershipPosition) -> None:
        old_leadership_position = self._query.filter(
            LeadershipPosition.leadership_positions_id == new_leadership_position.leadership_positions_id
        )
        old_leadership_position.update(
            {
                'code': new_leadership_position.code,
                'fullname': new_leadership_position.fullname,
            }
        )

        DBSession.commit()

    def get_leadership_position_by_id(self, id: int) -> LeadershipPosition:
        return self._query.get(id)
