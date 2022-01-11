from .model import MeasureUnit
from .repository import MeasureUnitRepository


class MeasureUnitService:

    def __init__(self):
        self.repo = MeasureUnitRepository()

    def get_all_measure_units(self) -> list:
        return self.repo.get_all_measure_units()

    def add_measure_unit(self, measure_unit: MeasureUnit) -> None:
        return self.repo.add_measure_unit(measure_unit)

    def get_measure_unit_by_id(self, id_: int) -> MeasureUnit:
        return self.repo.get_measure_unit_by_id(id_)

    def delete_measure_unit_by_id(self, id_: int) -> None:
        self.repo.delete_measure_unit_by_id(id_)

    def update_measure_unit(self, measure_unit: MeasureUnit) -> None:
        self.repo.update_measure_unit(measure_unit)
