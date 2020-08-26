from mks_backend.repositories.construction_repository import ConstructionRepository


class ConstructionService:
    def __init__(self):
        self.repo = ConstructionRepository()

    def get_all_constructions(self):
        return self.repo.get_all_constructions()

    def get_construction_by_id(self, id):
        return self.repo.get_construction_by_id(id)

    def add_construction(self, construction):
        return self.repo.add_construction(construction)

    def update_construction(self, new_construction):
        self.repo.update_construction(new_construction)

    def delete_construction_by_id(self, id):
        self.repo.delete_construction(id)

    def filter_constructions(self, params):
        return self.repo.filter_constructions(params)
