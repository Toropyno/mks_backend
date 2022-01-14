from typing import List

from mks_backend.session import DBSession

from .model import ObjectCompletion


class ObjectCompletionRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectCompletion)

    def get_object_completion_by_construction_object_id(self, construction_object_id: int) -> List[ObjectCompletion]:
        return self._query.filter(ObjectCompletion.construction_objects_id == construction_object_id).\
            order_by(ObjectCompletion.update_datetime).all()
