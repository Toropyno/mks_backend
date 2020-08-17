from mks_backend.models.construction_objects import ConstructionObjects
from mks_backend.repositories import DBSession


class ConstructionObjectRepository:

    @classmethod
    def get_construction_object_by_id(cls, id):
        return DBSession.query(ConstructionObjects).get(id)

    def get_all_construction_objects_by_construction_id(self, construction_id):
        return DBSession.query(ConstructionObjects).filter_by(construction_id=construction_id).all()

    def add_construction_object(self, construction_object):
        DBSession.add(construction_object)
        DBSession.commit()

    def delete_construction_object_by_id(self, id):
        construction_object = self.get_construction_object_by_id(id)
        DBSession.delete(construction_object)
        DBSession.commit()

    def update_construction_object(self, construction_object):
        DBSession.query(ConstructionObjects).filter_by(
            construction_object_id=construction_object.construction_object_id).update(
            {'construction_id': construction_object.construction_id,
             'object_code': construction_object.object_code,
             'object_name': construction_object.object_name,
             'zones_id': construction_object.zones_id,
             'object_categories_list_id': construction_object.object_categories_list_id,
             'planned_date': construction_object.planned_date,
             'weight': construction_object.weight,
             'generalplan_number': construction_object.generalplan_number,
             'building_volume': construction_object.building_volume,
             'floors_amount': construction_object.floors_amount,
             'construction_stages_id': construction_object.construction_stages_id})
        DBSession.commit()
