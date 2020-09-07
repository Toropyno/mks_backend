from mks_backend.models.construction_stages import ConstructionStages
from mks_backend.repositories.construction_stages_repository import ConstructionStageRepository


class ConstructionStageService:

    def __init__(self):
        self.repo = ConstructionStageRepository()

    def get_all_construction_stages(self) -> list:
        return self.repo.get_all_construction_stages()

    def get_construction_stage_by_id(self, id: int) -> ConstructionStages:
        return self.repo.get_construction_stage_by_id(id)

    def add_construction_stage(self, construction_stage: ConstructionStages) -> None:
        self.repo.add_construction_stage(construction_stage)

    def delete_construction_stage_by_id(self, id: int) -> None:
        self.repo.delete_construction_stage_by_id(id)

    def update_construction_stage(self, new_construction_stage: ConstructionStages) -> None:
        self.repo.update_construction_stage(new_construction_stage)
