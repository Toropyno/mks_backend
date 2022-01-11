from .model import MilitaryRank
from mks_backend.session import DBSession


class MilitaryRankRepository:

    def __init__(self):
        self._query = DBSession.query(MilitaryRank)

    def get_military_rank_by_id(self, id_: int) -> MilitaryRank:
        return self._query.get(id_)

    def get_all_military_ranks(self) -> list:
        return self._query.order_by(MilitaryRank.fullname).all()

    def add_military_rank(self, military_rank: MilitaryRank) -> None:
        DBSession.add(military_rank)
        DBSession.commit()

    def delete_military_rank_by_id(self, id_: int) -> None:
        self._query.filter_by(military_ranks_id=id_).delete()
        DBSession.commit()

    def update_military_rank(self, military_rank: MilitaryRank) -> None:
        self._query.filter_by(military_ranks_id=military_rank.military_ranks_id).update(
            {
                'fullname': military_rank.fullname,
            }
        )
        DBSession.commit()
