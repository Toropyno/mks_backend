from mks_backend.repositories.construction_repository import ConstructionRepository
from mks_backend.models.construction import Construction

from mks_backend.errors.db_basic_error import db_error_handler


class ConstructionService:
    def __init__(self):
        self.repo = ConstructionRepository()

    def get_all_constructions(self):
        return self.repo.get_all_constructions()

    def get_construction_by_id(self, id):
        return self.repo.get_construction_by_id(id)

    @db_error_handler
    def add_construction(self, construction):
        return self.repo.add_construction(construction)

    @db_error_handler
    def update_construction(self, new_construction):
        self.repo.update_construction(new_construction)

    def delete_construction_by_id(self, id):
        self.repo.delete_construction(id)

    def filter_constructions(self, params):
        return self.repo.filter_constructions(params)

    def convert_schema_to_object(self, schema):
        construction = Construction()

        construction.construction_id = schema.get('id')
        construction.project_code = schema.get('code')
        construction.project_name = schema.get('name')
        construction.construction_categories_id = schema.get('category')
        construction.subcategories_list_id = schema.get('subcategory')
        construction.is_critical = schema.get('isCritical')
        construction.commission_id = schema.get('commission')
        construction.idMU = schema.get('militaryUnit')
        construction.contract_date = schema.get('contractDate')
        construction.planned_date = schema.get('plannedDate')
        construction.object_amount = schema.get('objectsAmount')

        return construction
