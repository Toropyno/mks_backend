from mks_backend.models.organizations.military_rank import MilitaryRank
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class MilitaryRankRepository:

    def get_military_rank_by_id(self, id: int) -> MilitaryRank:
        return DBSession.query(MilitaryRank).get(id)

    def get_all_military_ranks(self) -> list:
        return DBSession.query(MilitaryRank).order_by(MilitaryRank.fullname).all()

    @db_error_handler
    def add_military_rank(self, military_rank: MilitaryRank) -> None:
        DBSession.add(military_rank)
        DBSession.commit()

    def delete_military_rank_by_id(self, id: int) -> None:
        DBSession.query(MilitaryRank).filter_by(military_ranks_id=id).delete()
        DBSession.commit()

    @db_error_handler
    def update_military_rank(self, military_rank: MilitaryRank) -> None:
        DBSession.query(MilitaryRank).filter_by(military_ranks_id=military_rank.military_ranks_id).update(
            {
                'fullname': military_rank.fullname,
            }
        )
        DBSession.commit()
