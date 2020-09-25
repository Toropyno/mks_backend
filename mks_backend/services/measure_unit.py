from mks_backend.models.measure_unit import MeasureUnit
from mks_backend.repositories.measure_unit import MeasureUnitRepository


class MeasureUnitService:

    def __init__(self):
        self.repo = MeasureUnitRepository()

    def get_all_measure_units(self) -> list:
        return self.repo.get_all_measure_units()

    def add_measure_unit(self, measure_unit: MeasureUnit) -> None:
        return self.repo.add_measure_unit(measure_unit)

    def get_measure_unit_by_id(self, id: int) -> MeasureUnit:
        return self.repo.get_measure_unit_by_id(id)

    def delete_measure_unit_by_id(self, id: int) -> None:
        self.repo.delete_measure_unit_by_id(id)

    def update_measure_unit(self, measure_unit: MeasureUnit) -> None:
        self.repo.update_measure_unit(measure_unit)
