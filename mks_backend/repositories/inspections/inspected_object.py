from typing import Tuple

from sqlalchemy import and_

from mks_backend.models.inspections.inspected_object import InspectedObject
from mks_backend.repositories import DBSession
from mks_backend.errors.db_basic_error import db_error_handler


class InspectedObjectRepository:

    def __init__(self):
        self._query = DBSession.query(InspectedObject)

    def delete_inspected_object(self, inspection_id: int, construction_id: int) -> None:
        self._query.filter(
            and_(InspectedObject.inspections_id == inspection_id, InspectedObject.construction_id == construction_id)
        ).delete()
        DBSession.commit()

    @db_error_handler
    def add_inspected_objects(self, inspected_objects: Tuple[InspectedObject]) -> None:
        for inspected_object in inspected_objects:
            DBSession.merge(inspected_object)
        DBSession.commit()
