from mks_backend.models.construction_stage import ConstructionStage
from mks_backend.repositories.construction_stage_repository import ConstructionStageRepository


class ConstructionStageService:

    def __init__(self):
        self.repo = ConstructionStageRepository()

    def get_all_construction_stages(self) -> list:
        return self.repo.get_all_construction_stages()

    def get_construction_stage_by_id(self, id: int) -> ConstructionStage:
        return self.repo.get_construction_stage_by_id(id)

    def add_construction_stage(self, construction_stage: ConstructionStage) -> None:
        self.repo.add_construction_stage(construction_stage)

    def delete_construction_stage_by_id(self, id: int) -> None:
        self.repo.delete_construction_stage_by_id(id)

    def update_construction_stage(self, new_construction_stage: ConstructionStage) -> None:
        self.repo.update_construction_stage(new_construction_stage)
