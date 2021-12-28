from .model import RealtyType
from .repository import RealtyTypeRepository


class RealtyTypeService:

    def __init__(self):
        self.repo = RealtyTypeRepository()

    def get_all_realty_types(self) -> list:
        return self.repo.get_all_realty_types()

    def get_realty_type_by_id(self, id_: int) -> RealtyType:
        return self.repo.get_realty_type_by_id(id_)

    def add_realty_type(self, realty_type: RealtyType) -> None:
        self.repo.add_realty_type(realty_type)

    def update_realty_type(self, new_realty_type: RealtyType) -> None:
        self.repo.update_realty_type(new_realty_type)

    def delete_realty_type_by_id(self, id_: int) -> None:
        self.repo.delete_realty_type_by_id(id_)
