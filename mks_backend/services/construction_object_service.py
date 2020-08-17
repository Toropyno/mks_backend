from mks_backend.models.construction_objects import ConstructionObjects
from mks_backend.repositories.construction_objects_repository import ConstructionObjectRepository


class ConstructionObjectService:

    def __init__(self):
        self.repo = ConstructionObjectRepository()

    def get_all_construction_objects_by_construction_id(self, construction_id):
        return self.repo.get_all_construction_objects_by_construction_id(construction_id)

    def get_construction_object_by_id(self, id):
        return self.repo.get_construction_object_by_id(id)

    def add_construction_object(self, construction_object):
        self.repo.add_construction_object(construction_object)

    def delete_construction_object_by_id(self, id):
        self.repo.delete_construction_object_by_id(id)

    def update_construction_object(self, new_construction_object):
        self.repo.update_construction_object(new_construction_object)

    def get_object(self, json_body):
        construction_object = ConstructionObjects()
        if 'id' in json_body:
            construction_object.construction_objects_id = json_body['id']

        construction_object.construction_id = json_body['constructionId']
        construction_object.object_code = json_body['objectCode']
        construction_object.object_name = json_body['objectName']
        construction_object.zones_id = json_body['zonesId']
        construction_object.object_categories_list_id = json_body['objectCategoriesListId']
        construction_object.planned_date = json_body['plannedDate']
        construction_object.weight = json_body['weight']
        construction_object.generalplan_number = json_body['generalPlanNumber']
        construction_object.building_volume = json_body['buildingVolume']
        construction_object.floors_amount = json_body['floorsAmount']
        construction_object.construction_stages_id = json_body['constructionStagesId']
        return construction_object
