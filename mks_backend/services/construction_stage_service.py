from mks_backend.repositories.construction_stages_repository import ConstructionStageRepository


class ConstructionStageService:

    def __init__(self):
        self.repo = ConstructionStageRepository()

    def get_all_construction_stages(self):
        return self.repo.get_all_construction_stages()

    def get_construction_stage_by_id(self, id):
        return self.repo.get_construction_stage_by_id(id)

    def add_construction_stage(self, construction_stage):
        if self.repo.get_construction_stage_by_code(construction_stage.code):
            raise ValueError('Этап строительства с таким кратким наименованием уже существует.')
        if self.repo.get_construction_stage_by_fullname(construction_stage.fullname):
            raise ValueError('Этап строительства с таким полным наименованием уже существует.')
        self.repo.add_construction_stage(construction_stage)

    def delete_construction_stage_by_id(self, id):
        self.repo.delete_construction_stage_by_id(id)

    def update_construction_stage(self, new_construction_stage):
        self.repo.update_construction_stage(new_construction_stage)