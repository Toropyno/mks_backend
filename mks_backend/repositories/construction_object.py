from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.construction_object import ConstructionObject
from mks_backend.repositories import DBSession


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
        # DBSession.commit()
        DBSession.query(ConstructionObject).filter_by(
            construction_objects_id=construction_object.construction_objects_id).update(
            {
                'construction_id': construction_object.construction_id,
                'object_code': construction_object.object_code,
                'object_name': construction_object.object_name,
                'zones_id': construction_object.zones_id,
                'object_categories_list_id': construction_object.object_categories_list_id,
                'planned_date': construction_object.planned_date,
                'weight': construction_object.weight,
                'generalplan_number': construction_object.generalplan_number,
                'building_volume': construction_object.building_volume,
                'floors_amount': construction_object.floors_amount,
                'construction_stages_id': construction_object.construction_stages_id,
                'coordinates_id': construction_object.coordinates_id,
                'realty_types_id': construction_object.realty_types_id,
                'fact_date': construction_object.fact_date,
            }
        )
        DBSession.commit()
