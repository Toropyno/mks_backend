from typing import List

from sqlalchemy import not_

from mks_backend.models.inspections.inspection import Inspection
from mks_backend.models.inspections.inspected_object import InspectedObject
from mks_backend.models.constructions import Construction
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class InspectionRepository:

    def __init__(self):
        self._query = DBSession.query(Inspection)

    def get_all_inspections(self) -> List[Inspection]:
        return self._query.order_by(Inspection.insp_date).all()

    @db_error_handler
    def add_inspection(self, inspection: Inspection) -> None:
        DBSession.add(inspection)
        DBSession.commit()

    def delete_inspection_by_id(self, id: int) -> None:
        self._query.filter(Inspection.inspections_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_inspection(self, new_inspection: Inspection) -> None:
        old_inspection = self._query.filter(Inspection.inspections_id == new_inspection.inspections_id)
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
        filtered_inspections = self._query.outerjoin(InspectedObject, Construction)

        if 'date_start' in params:
            date_start = params['date_start']
            filtered_inspections = filtered_inspections.filter(Inspection.insp_date >= date_start)
        if 'date_end' in params:
            date_end = params['date_end']
            filtered_inspections = filtered_inspections.filter(Inspection.insp_date <= date_end)
        if 'name' in params:
            name = params['name']
            filtered_inspections = filtered_inspections.filter(Inspection.insp_name.ilike('%{}%'.format(name)))
        if 'inspector' in params:
            inspector = params['inspector']
            filtered_inspections = filtered_inspections.filter(Inspection.inspector.ilike('%{}%'.format(inspector)))
        if 'construction_code' in params:
            construction_code = params['construction_code']
            filtered_inspections = filtered_inspections.filter(
                Construction.project_code.ilike('%{}%'.format(construction_code))
            )
        if 'have_file' in params:
            have_file = params['have_file']
            if have_file:
                filtered_inspections = filtered_inspections.filter(Inspection.files)
            else:
                filtered_inspections = filtered_inspections.filter(not_(Inspection.files.any()))
        if 'have_inspected_objects' in params:
            have_inspected_objects = params['have_inspected_objects']
            if have_inspected_objects:
                filtered_inspections = filtered_inspections.filter(Inspection.constructions)
            else:
                filtered_inspections = filtered_inspections.filter(not_(Inspection.constructions.any()))

        # TODO: add FIAS Subject field

        return filtered_inspections.order_by(Inspection.insp_date).all()
