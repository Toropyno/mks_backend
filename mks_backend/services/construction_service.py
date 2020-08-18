from mks_backend.repositories.construction_repository import ConstructionRepository
from mks_backend.models.construction import Construction


class ConstructionService:
    def __init__(self):
        self.repo = ConstructionRepository()

    def get_all_constructions(self):
        return self.repo.get_all_constructions()

    def get_construction_by_id(self, id):
        return self.repo.get_construction_by_id(id)

    def add_construction(self, construction):
        if self.repo.get_construction_by_project_code(construction.project_code):
            raise ValueError('Проект с таким кодом уже существует')
        else:
            return self.repo.add_construction(construction)

    def update_construction(self, new_construction):
        old_construction = self.repo.get_construction_by_id(new_construction.construction_id)

        if old_construction.project_code != new_construction.project_code:
            if self.repo.get_construction_by_project_code(new_construction.project_code):
                raise ValueError('Проект с таим кодом уже существует')

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
