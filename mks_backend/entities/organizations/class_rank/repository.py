from .model import ClassRank
from mks_backend.session import DBSession


class ClassRankRepository:

    def __init__(self):
        self._query = DBSession.query(ClassRank)

    def get_class_rank_by_id(self, id_: int) -> ClassRank:
        return self._query.get(id_)

    def get_all_class_ranks(self) -> list:
        return self._query.order_by(ClassRank.fullname).all()

    def add_class_rank(self, class_rank: ClassRank) -> None:
        DBSession.add(class_rank)
        DBSession.commit()

    def delete_class_rank(self, id: int) -> None:
        self._query.filter_by(class_ranks_id=id).delete()
        DBSession.commit()

    def edit_class_rank(self, class_rank: ClassRank) -> None:
        self._query.filter_by(class_ranks_id=class_rank.class_ranks_id).update(
            {
                'fullname': class_rank.fullname,
            }
        )
        DBSession.commit()
