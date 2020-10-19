from typing import List

from mks_backend.models.inspections.inspection import Inspection
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class InspectionRepository:

    def __init__(self):
        self._query = DBSession.query(Inspection)

    def get_all_inspections(self) -> List[Inspection]:
        return self._query.all()

    @db_error_handler
    def add_inspection(self, inspection: Inspection) -> None:
        DBSession.add(inspection)
        DBSession.commit()

    def delete_inspection_by_id(self, id: int) -> None:
        self._query.filter(Inspection.inspections_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_inspection(self, new_inspection: Inspection) -> None:
        old_inspection = self._query.filter(
            Inspection.inspections_id == new_inspection.inspections_id
        )
        old_inspection.update(
            {
                'insp_date': new_inspection.insp_date,
                'insp_name': new_inspection.insp_name,
                'inspector': new_inspection.inspector,
                'insp_result': new_inspection.insp_result,
            }
        )

        DBSession.commit()

    def get_inspection_by_id(self, id: int) -> Inspection:
        return self._query.get(id)

    def get_filtered_inspections(self, params: dict) -> List[Inspection]:
        # TODO: rework with MKSBRYANS-227
        return self._query.all()
