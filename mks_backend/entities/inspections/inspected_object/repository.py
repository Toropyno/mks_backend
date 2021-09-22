from typing import Tuple

from sqlalchemy import and_

from .model import InspectedObject
from mks_backend.session import DBSession


class InspectedObjectRepository:

    def __init__(self):
        self._query = DBSession.query(InspectedObject)

    def delete_inspected_object(self, inspection_id: int, construction_id: int) -> None:
        self._query.filter(
            and_(InspectedObject.inspections_id == inspection_id, InspectedObject.construction_id == construction_id)
        ).delete()
        DBSession.commit()

    def add_inspected_objects(self, inspected_objects: Tuple[InspectedObject]) -> None:
        for inspected_object in inspected_objects:
            DBSession.merge(inspected_object)
        DBSession.commit()
