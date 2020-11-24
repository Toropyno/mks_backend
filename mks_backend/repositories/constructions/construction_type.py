from mks_backend.models.constructions import ConstructionType
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class ConstructionTypeRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionType)

    def get_all_construction_types(self) -> list:
        return self._query.order_by(ConstructionType.fullname).all()

    @db_error_handler
    def add_construction_type(self, construction_type: ConstructionType) -> None:
        DBSession.add(construction_type)
        DBSession.commit()

    def delete_construction_type_by_id(self, id: int) -> None:
        self._query.filter(ConstructionType.construction_types_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_construction_type(self, new_construction_type: ConstructionType) -> None:
        DBSession.merge(new_construction_type)
        DBSession.commit()

    def get_construction_type_by_id(self, id: int) -> ConstructionType:
        return self._query.get(id)
