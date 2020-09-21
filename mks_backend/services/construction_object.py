from mks_backend.models.construction_object import ConstructionObject
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.services.construction_document import ConstructionDocumentService
from mks_backend.services.location import LocationService
from mks_backend.services.object_category_list import ObjectCategoryListService
# from mks_backend.services.construction_progress import ConstructionProgressService


class ConstructionObjectService:

    def __init__(self):
        self.repo = ConstructionObjectRepository()
        self.location_service = LocationService()
        self.object_categories_list_service = ObjectCategoryListService()
        self.construction_document_service = ConstructionDocumentService()
        # self.construction_progress_service = ConstructionProgressService()

    def get_all_construction_objects_by_construction_id(self, construction_id: int) -> list:
        construction_objects = self.repo.get_all_construction_objects_by_construction_id(construction_id)

        # for construction_object in construction_objects:
        #     construction_object.construction_progress = \
        #         self.construction_progress_service.get_construction_progress_for_construction_objects(
        #             construction_object.construction_progress
        #         )

        return construction_objects

    def get_construction_object_by_id(self, id: int) -> ConstructionObject:
        construction_object = self.repo.get_construction_object_by_id(id)

        # construction_object.construction_progress = \
        #     self.construction_progress_service.get_construction_progress_for_construction_objects(
        #         construction_object.construction_progress
        #     )

        return construction_object

    def add_construction_object(self, construction_object: ConstructionObject) -> None:
        self.repo.add_construction_object(construction_object)

    def delete_construction_object_by_id(self, id: int) -> None:
        self.repo.delete_construction_object_by_id(id)

    def update_construction_object(self, new_construction_object: ConstructionObject) -> None:
        self.location_service.add_or_update_location(new_construction_object.location)
        self.repo.update_construction_object(new_construction_object)

    def convert_schema_to_object(self, schema: dict) -> ConstructionObject:
        construction_object = ConstructionObject()
        if 'id' in schema:
            construction_object.construction_objects_id = schema.get('id')

        construction_object.construction_id = schema.get('projectId')
        construction_object.object_code = schema.get('code')
        construction_object.object_name = schema.get('name')

        zone_id = schema.get('zone')
        construction_object.zones_id = zone_id

        object_category_id = schema.get('category')
        if object_category_id:
            object_categories_list = self.object_categories_list_service.get_object_categories_list_by_relations(
                zone_id, object_category_id
            )
            construction_object.object_categories_list_id = object_categories_list.object_categories_list_id

        construction_documents = schema.get('constructionDocument', [])
        if construction_documents is not None:
            construction_documents_ids = list(map(lambda x: x['id'], construction_documents))
            construction_object.construction_documents = \
                self.construction_document_service.get_many_construction_documents_by_id(
                    construction_documents_ids
                )

        construction_object.planned_date = schema.get('plannedDate')
        construction_object.weight = schema.get('weight')
        construction_object.generalplan_number = schema.get('generalPlanNumber')
        construction_object.building_volume = schema.get('buildingVolume')
        construction_object.floors_amount = schema.get('floorsAmount')
        construction_object.construction_stages_id = schema.get('stage')
        construction_object.coordinates_id = schema.get('locationId')
        construction_object.realty_types_id = schema.get('realtyTypeId')
        construction_object.fact_date = schema.get('factDate')

        return construction_object
