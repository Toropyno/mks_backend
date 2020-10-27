from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.work_list.element_type import ElementType
from mks_backend.repositories import DBSession


class ElementTypeRepository:

    def get_all_element_types(self) -> list:
        return DBSession.query(ElementType).all()

    @db_error_handler
    def add_element_type(self, element_type: ElementType) -> None:
        DBSession.add(element_type)
        DBSession.commit()

    def get_element_type_by_id(self, id: int) -> ElementType:
        return DBSession.query(ElementType).get(id)

    @db_error_handler
    def update_element_type(self, element_type: ElementType) -> None:
        DBSession.query(ElementType).filter_by(element_types_id=element_type.element_types_id).update(
            {
                'fullName': element_type.fullname,
            }
        )
        DBSession.commit()

    def delete_element_type_by_id(self, id: int) -> None:
        element_type = self.get_element_type_by_id(id)
        DBSession.delete(element_type)
        DBSession.commit()
