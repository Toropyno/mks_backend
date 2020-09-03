from mks_backend.repositories.military_unit_repository import MilitaryUnitRepository


class MilitaryUnitService:
    def __init__(self):
        self.repo = MilitaryUnitRepository()

    def get_all_military_units(self):
        return self.repo.get_all_military_units()

    def get_root_military_units(self):
        return self.repo.get_root_military_units()