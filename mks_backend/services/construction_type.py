from mks_backend.models.construction_type import ConstructionType
from mks_backend.repositories.construction_type import ConstructionTypeRepository


class ConstructionTypeService:
    def __init__(self):
        self.repo = ConstructionTypeRepository()

    def get_all_construction_types(self) -> list:
        return self.repo.get_all_construction_types()

    def get_construction_type_by_id(self, id: int) -> ConstructionType:
        return self.repo.get_construction_type_by_id(id)

    def add_construction_type(self, construction_type: ConstructionType) -> None:
        self.repo.add_construction_type(construction_type)

    def update_construction_type(self, new_construction_type: ConstructionType) -> None:
        self.repo.update_construction_type(new_construction_type)

    def delete_construction_type_by_id(self, id: int) -> None:
        self.repo.delete_construction_type_by_id(id)
