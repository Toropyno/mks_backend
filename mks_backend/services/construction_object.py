from mks_backend.models.construction_object import ConstructionObject
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.services.construction_progress import ConstructionProgressService
from mks_backend.services.coordinate import CoordinateService
from mks_backend.services.documents.construction_document import ConstructionDocumentService
from mks_backend.services.filestorage import FilestorageService
from mks_backend.services.object_category_list import ObjectCategoryListService


class ConstructionObjectService:

    def __init__(self):
        self.repo = ConstructionObjectRepository()
        self.coordinate_service = CoordinateService()
        self.object_categories_list_service = ObjectCategoryListService()
        self.construction_document_service = ConstructionDocumentService()
        self.progress_service = ConstructionProgressService()
        self.file_storage_service = FilestorageService()

    def get_all_construction_objects_by_construction_id(self, construction_id: int) -> list:
        construction_objects = self.repo.get_all_construction_objects_by_construction_id(construction_id)
        return construction_objects

    def get_construction_object_by_id(self, id: int):
        construction_object = self.repo.get_construction_object_by_id(id)
        return construction_object

    def add_construction_object(self, construction_object: ConstructionObject) -> None:
        self.repo.add_construction_object(construction_object)

    def delete_construction_object_by_id(self, id: int) -> None:
        self.repo.delete_construction_object_by_id(id)

    def update_construction_object(self, new_construction_object: ConstructionObject) -> None:
        self.coordinate_service.add_or_update_coordinate(new_construction_object.coordinate)
        self.repo.update_construction_object(new_construction_object)

    def convert_schema_to_object(self, schema: dict) -> ConstructionObject:
        construction_object_id = schema.get('id')
        if construction_object_id:
            construction_object = self.get_construction_object_by_id(construction_object_id)
        else:
            construction_object = ConstructionObject()

        construction_object.construction_id = schema.get('projectId')
        construction_object.object_code = schema.get('code')
        construction_object.object_name = schema.get('name')
        construction_object.planned_date = schema.get('plannedDate')
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

        construction_documents = schema.get('documents')
        if construction_documents:
            construction_documents_ids = list(map(lambda x: x['id'], construction_documents))
            construction_object.documents = \
                self.construction_document_service.get_many_construction_documents_by_id(
                    construction_documents_ids
                )

        file_storage = schema.get('files')
        if file_storage:
            file_storage_ids = list(map(lambda x: x['id'], file_storage))
            construction_object.file_storage = \
                self.file_storage_service.get_many_file_storages_by_id(
                    file_storage_ids
                )

        return construction_object
