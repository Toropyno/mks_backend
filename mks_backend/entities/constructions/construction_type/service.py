from .model import ConstructionType
from .repository import ConstructionTypeRepository


class ConstructionTypeService:

    def __init__(self):
        self.repo = ConstructionTypeRepository()

    def get_all_construction_types(self) -> list:
        return self.repo.get_all_construction_types()

    def get_construction_type_by_id(self, id_: int) -> ConstructionType:
        return self.repo.get_construction_type_by_id(id_)

    def add_construction_type(self, construction_type: ConstructionType) -> None:
        self.repo.add_construction_type(construction_type)

    def update_construction_type(self, new_construction_type: ConstructionType) -> None:
        self.repo.update_construction_type(new_construction_type)

    def delete_construction_type_by_id(self, id_: int) -> None:
        self.repo.delete_construction_type_by_id(id_)
