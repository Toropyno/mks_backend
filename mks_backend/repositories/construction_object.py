from mks_backend.models.construction_object import ConstructionObject
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class ConstructionObjectRepository:

    def get_construction_object_by_id(self, id: int) -> ConstructionObject:
        return DBSession.query(ConstructionObject).get(id)

    def get_all_construction_objects_by_construction_id(self, construction_id) -> list:
        return DBSession.query(ConstructionObject).filter_by(construction_id=construction_id). \
            order_by(ConstructionObject.planned_date).all()

    @db_error_handler
    def add_construction_object(self, construction_object: ConstructionObject) -> None:
        DBSession.add(construction_object)
        DBSession.commit()

    def delete_construction_object_by_id(self, id: int) -> None:
        construction_object = self.get_construction_object_by_id(id)
        DBSession.delete(construction_object)
        DBSession.commit()

    @db_error_handler
    def update_construction_object(self, construction_object: ConstructionObject) -> None:
        DBSession.commit()
