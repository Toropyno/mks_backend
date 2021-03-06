from mks_backend.session import DBSession

from .model import ConstructionObject


class ConstructionObjectRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionObject)

    def get_construction_object_by_id(self, id_: int) -> ConstructionObject:
        return self._query.get(id_)

    def get_all_construction_objects_by_construction_id(self, construction_id) -> list:
        return self._query.filter_by(construction_id=construction_id). \
            order_by(ConstructionObject.object_code).all()

    def add_construction_object(self, construction_object: ConstructionObject) -> None:
        DBSession.add(construction_object)
        DBSession.commit()

    def delete_construction_object_by_id(self, id_: int) -> None:
        construction_object = self.get_construction_object_by_id(id_)
        DBSession.delete(construction_object)
        DBSession.commit()

    def update_construction_object(self, construction_object: ConstructionObject) -> None:
        DBSession.commit()
