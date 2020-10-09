from datetime import datetime

from mks_backend.models.construction_object import ConstructionObject
from mks_backend.repositories.construction_object import ConstructionObjectRepository
from mks_backend.services.documents.construction_document import ConstructionDocumentService
from mks_backend.services.coordinate import CoordinateService
from mks_backend.services.construction_progress import ConstructionProgressService
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

        zone_id = schema.get('zone')
        construction_object.zones_id = zone_id

        object_category_id = schema.get('category')
        if object_category_id:
            object_categories_list = self.object_categories_list_service.get_object_categories_list_by_relations(
                zone_id, object_category_id
            )
            construction_object.object_categories_list_id = object_categories_list.object_categories_list_id

        construction_documents = schema.get('documents', [])
        if construction_documents is not None:
            construction_documents_ids = list(map(lambda x: x['id'], construction_documents))
            construction_object.documents = \
                self.construction_document_service.get_many_construction_documents_by_id(
                    construction_documents_ids
                )

        file_storage = schema.get('files', [])
        if file_storage is not None:
            file_storage_ids = list(map(lambda x: x['id'], file_storage))
            construction_object.file_storage = \
                self.file_storage_service.get_many_file_storages_by_id(
                    file_storage_ids
                )

        construction_object.planned_date = schema.get('plannedDate')
        construction_object.weight = schema.get('weight')
        construction_object.generalplan_number = schema.get('generalPlanNumber')
        construction_object.building_volume = schema.get('buildingVolume')
        construction_object.floors_amount = schema.get('floorsAmount')
        construction_object.construction_stages_id = schema.get('stage')
        construction_object.coordinates_id = schema.get('coordinateId')
        construction_object.realty_types_id = schema.get('realtyType')
        construction_object.fact_date = schema.get('factDate')

        return construction_object

    def get_construction_objects_calculated(self, id: int) -> dict:
        plan = 0
        actually = 0
        entered_additionally = 0
        readiness = 0
        workers = 0
        equipment = 0

        now_year = datetime.now().year
        construction_objects = self.get_all_construction_objects_by_construction_id(id)

        for constr_object in construction_objects:
            plan += check_planned_year_is_now_year(constr_object.planned_date.year, now_year)
            actually += check_actually_entered(constr_object, now_year)
            entered_additionally += check_entered_additionally(constr_object, now_year)

            progress = self.get_progress_calculated(constr_object)
            if progress:
                readiness += progress.get('readiness')
                workers += progress.get('workers')
                equipment += progress.get('equipment')

        return {
            'plan': plan,
            'actually': actually,
            'difference': abs(plan - actually),
            'entered_additionally': entered_additionally,
            'readiness': readiness,
            'workers': workers,
            'equipment': equipment,
        }

    def get_progress_calculated(self, constr_object):
        last_construction_progress = self.progress_service.get_construction_progress_by_object_last_reporting_date(
            constr_object.construction_objects_id
        )
        if last_construction_progress:
            return {
                'readiness': float(last_construction_progress.readiness) * 0.01 * constr_object.weight,
                'workers': last_construction_progress.people,
                'equipment': last_construction_progress.equipment,
            }


def check_planned_year_is_now_year(planned_year, now_year):
    if planned_year == now_year:
        return 1
    return 0


def check_actually_entered(constr_object, now_year):
    constr_object.fact_date = constr_object.planned_date
    # remove co.fact_date = co.planned_date, after added fact_date in frontend

    if constr_object.fact_date:
        if (constr_object.planned_date.year == now_year) and (constr_object.fact_date.year == now_year):
            return 1
    return 0


def check_entered_additionally(constr_object, now_year):
    constr_object.fact_date = constr_object.planned_date
    # remove co.fact_date = co.planned_date, after added fact_date in frontend

    if constr_object.fact_date:
        if (constr_object.planned_date.year != now_year) and (constr_object.fact_date.year == now_year):
            return 1
    return 0
