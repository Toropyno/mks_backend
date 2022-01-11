from .model import ConstructionStage
from .repository import ConstructionStageRepository


class ConstructionStageService:

    def __init__(self):
        self.repo = ConstructionStageRepository()

    def get_all_construction_stages(self) -> list:
        return self.repo.get_all_construction_stages()

    def get_construction_stage_by_id(self, id_: int) -> ConstructionStage:
        return self.repo.get_construction_stage_by_id(id_)

    def add_construction_stage(self, construction_stage: ConstructionStage) -> None:
        self.repo.add_construction_stage(construction_stage)

    def delete_construction_stage_by_id(self, id_: int) -> None:
        self.repo.delete_construction_stage_by_id(id_)

    def update_construction_stage(self, new_construction_stage: ConstructionStage) -> None:
        self.repo.update_construction_stage(new_construction_stage)
