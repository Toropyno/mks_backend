from typing import List

from .model import ReferenceHistory
from mks_backend.session import DBSession


class ReferenceHistoryRepository:

    def __init__(self):
        self._query = DBSession.query(ReferenceHistory)

    def get_reference_history_by_construction_object_id(self, construction_object_id: int) -> List[ReferenceHistory]:
        return self._query.filter(ReferenceHistory.construction_objects_id == construction_object_id).\
            order_by(ReferenceHistory.end_date).all()
