from mks_backend.entities.construction_objects.object_category_list import ObjectCategoryListService
from mks_backend.entities.coordinate import CoordinateService

from .model import ConstructionObject
from .repository import ConstructionObjectRepository


class ConstructionObjectService:

    def __init__(self):
        self.repo = ConstructionObjectRepository()
        self.coordinate_service = CoordinateService()
        self.object_categories_list_service = ObjectCategoryListService()

    def get_all_construction_objects_by_construction_id(self, construction_id: int) -> list:
        construction_objects = self.repo.get_all_construction_objects_by_construction_id(construction_id)
        return construction_objects

    def get_construction_object_by_id(self, id_: int):
        construction_object = self.repo.get_construction_object_by_id(id_)
        return construction_object

    def add_construction_object(self, construction_object: ConstructionObject) -> None:
        self.repo.add_construction_object(construction_object)

    def delete_construction_object_by_id(self, id_: int) -> None:
        self.repo.delete_construction_object_by_id(id_)

    def update_construction_object(self, new_construction_object: ConstructionObject) -> None:
        self.coordinate_service.add_or_update_coordinate(new_construction_object.coordinate)
        self.repo.update_construction_object(new_construction_object)

    def to_mapped_object(self, schema: dict) -> ConstructionObject:
        construction_object_id = schema.get('id')
        if construction_object_id:
            construction_object = self.get_construction_object_by_id(construction_object_id)
        else:
            construction_object = ConstructionObject()

        construction_object.construction_id = schema.get('projectId')
        construction_object.object_code = schema.get('code')
        construction_object.object_name = schema.get('name')
        construction_object.weight = schema.get('weight')
        construction_object.generalplan_number = schema.get('generalPlanNumber')
        construction_object.building_volume = schema.get('buildingVolume')
        construction_object.floors_amount = schema.get('floorsAmount')
        construction_object.construction_stages_id = schema.get('stage')
        construction_object.coordinates_id = schema.get('coordinateId')
        construction_object.realty_types_id = schema.get('realtyType')
        construction_object.fact_date = schema.get('factDate')

        zone_id = schema.get('zone')
        construction_object.zones_id = zone_id

        object_category_id = schema.get('category')
        if object_category_id:
            object_categories_list = self.object_categories_list_service.get_object_categories_list_by_relations(
                zone_id, object_category_id
            )
            construction_object.object_categories_list_id = object_categories_list.object_categories_list_id

        return construction_object
