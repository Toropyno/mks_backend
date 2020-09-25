from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.measure_unit import MeasureUnit
from mks_backend.repositories import DBSession


class MeasureUnitRepository:

    def get_all_measure_units(self) -> list:
        return DBSession.query(MeasureUnit).all()

    @db_error_handler
    def add_measure_unit(self, measure_unit: MeasureUnit) -> None:
        DBSession.add(measure_unit)
        DBSession.commit()

    def get_measure_unit_by_id(self, id: int) -> MeasureUnit:
        return DBSession.query(MeasureUnit).get(id)

    @db_error_handler
    def update_measure_unit(self, measure_unit: MeasureUnit) -> None:
        DBSession.query(MeasureUnit).filter_by(unit_id=measure_unit.unit_id).update(
            {
                'unit_code': measure_unit.unit_code,
                'unit_name': measure_unit.unit_name,
            }
        )
        DBSession.commit()

    def delete_measure_unit_by_id(self, id: int) -> None:
        measure_unit = self.get_measure_unit_by_id(id)
        DBSession.delete(measure_unit)
        DBSession.commit()
