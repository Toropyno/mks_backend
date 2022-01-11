from .model import MeasureUnit
from mks_backend.session import DBSession


class MeasureUnitRepository:

    def __init__(self):
        self._query = DBSession.query(MeasureUnit)

    def get_all_measure_units(self) -> list:
        return self._query.all()

    def add_measure_unit(self, measure_unit: MeasureUnit) -> None:
        DBSession.add(measure_unit)
        DBSession.commit()

    def get_measure_unit_by_id(self, id_: int) -> MeasureUnit:
        return self._query.get(id_)

    def update_measure_unit(self, measure_unit: MeasureUnit) -> None:
        self._query.filter_by(unit_id=measure_unit.unit_id).update(
            {
                'unit_code': measure_unit.unit_code,
                'unit_name': measure_unit.unit_name,
            }
        )
        DBSession.commit()

    def delete_measure_unit_by_id(self, id_: int) -> None:
        measure_unit = self.get_measure_unit_by_id(id_)
        DBSession.delete(measure_unit)
        DBSession.commit()
