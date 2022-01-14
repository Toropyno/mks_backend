from typing import List

from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.session import DBSession

from .model import ClassRank


class ClassRankRepository:

    def __init__(self):
        self._query = DBSession.query(ClassRank)

    def get_class_rank_by_id(self, id_: int) -> ClassRank:
        class_rank = self._query.get(id_)
        if not class_rank:
            raise DBBasicError('class_rank_nf')
        return class_rank

    def get_all_class_ranks(self) -> List[ClassRank]:
        return self._query.order_by(ClassRank.fullname).all()

    def add_class_rank(self, class_rank: ClassRank) -> None:
        DBSession.add(class_rank)
        DBSession.commit()

    def delete_class_rank(self, id: int) -> None:
        self._query.filter_by(class_ranks_id=id).delete()
        DBSession.commit()

    def update_class_rank(self, class_rank: ClassRank) -> None:
        if DBSession.merge(class_rank) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('class_rank_ad')
