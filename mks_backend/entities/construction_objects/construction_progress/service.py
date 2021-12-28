from .model import ConstructionProgress
from .repository import ConstructionProgressRepository


class ConstructionProgressService:

    def __init__(self):
        self.repo = ConstructionProgressRepository()

    def get_construction_progress_by_id(self, id_: int) -> ConstructionProgress:
        return self.repo.get_construction_progress_by_id(id_)

    def add_construction_progress(self, construction_progress: ConstructionProgress) -> None:
        self.repo.add_construction_progress(construction_progress)

    def delete_construction_progress_by_id(self, id_: int) -> None:
        construction_progress = self.get_construction_progress_by_id(id_)
        self.repo.delete_construction_progress(construction_progress)

    def update_construction_progress(self, construction_progress: ConstructionProgress) -> None:
        self.repo.update_construction_progress(construction_progress)

    def get_all_construction_progresses_by_object(self, objects_id: int):
        construction_progresses = self.repo.get_all_construction_progresses_by_object(objects_id)
        return construction_progresses

    def get_last_construction_progress_by_object(self, objects_id: int):
        return self.repo.get_last_construction_progress_by_object(objects_id)
