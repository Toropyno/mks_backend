from mks_backend.models.work_list.element_type import ElementType
from mks_backend.session import DBSession


class ElementTypeRepository:

    def __init__(self):
        self._query = DBSession.query(ElementType)

    def get_all_element_types(self) -> list:
        return self._query.all()

    def add_element_type(self, element_type: ElementType) -> None:
        DBSession.add(element_type)
        DBSession.commit()

    def get_element_type_by_id(self, id: int) -> ElementType:
        return self._query.get(id)

    def update_element_type(self, element_type: ElementType) -> None:
        self._query.filter_by(element_types_id=element_type.element_types_id).update(
            {
                'fullName': element_type.fullname,
            }
        )
        DBSession.commit()

    def delete_element_type_by_id(self, id: int) -> None:
        element_type = self.get_element_type_by_id(id)
        DBSession.delete(element_type)
        DBSession.commit()
