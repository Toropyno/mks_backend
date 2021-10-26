from datetime import date
from .repository import MilitaryUnitExtensionRepository


class MilitaryUnitExtensionService:

    def __init__(self):
        self.repo = MilitaryUnitExtensionRepository()

    def get_all_military_unit_extensions(self) -> list:
        return self.repo.get_all_military_unit_extensions()

    def get_military_unit_extension_by_id(self, id: int):
        return self.repo.get_military_unit_extension_by_id(id)

    def add_military_unit_extension(self, military_unit_extension) -> None:
        self.repo.add_military_unit_extension(military_unit_extension)

    def update_military_unit_extension(self, new_military_unit_extension) -> None:
        self.repo.update_military_unit_extension(new_military_unit_extension)

    def delete_military_unit_extension_by_id(self, id: int, date: date) -> None:
        self.repo.delete_military_unit_extension_by_id(id, date)
