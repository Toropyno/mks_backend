from .model import ElementType
from .repository import ElementTypeRepository


class ElementTypeService:

    def __init__(self):
        self.repo = ElementTypeRepository()

    def get_all_element_types(self) -> list:
        return self.repo.get_all_element_types()

    def get_element_type_by_id(self, id: int) -> ElementType:
        return self.repo.get_element_type_by_id(id)

    def add_element_type(self, element_type: ElementType) -> None:
        self.repo.add_element_type(element_type)

    def update_element_type(self, new_element_type: ElementType) -> None:
        self.repo.update_element_type(new_element_type)

    def delete_element_type_by_id(self, id: int) -> None:
        self.repo.delete_element_type_by_id(id)
