from mks_backend.models.construction_progress import ConstructionProgress
from mks_backend.repositories.construction_progress import ConstructionProgressRepository
from datetime import datetime


class ConstructionProgressService:

    def __init__(self):
        self.repo = ConstructionProgressRepository()

    def get_all_construction_progresses(self) -> list:
        return self.repo.get_all_construction_progresses()

    def get_construction_progress_by_id(self, id: int) -> ConstructionProgress:
        return self.repo.get_construction_progress_by_id(id)

    def add_construction_progress(self, construction_progress: ConstructionProgress) -> None:
        self.repo.add_construction_progress(construction_progress)

    def delete_construction_progress_by_id(self, id: int) -> None:
        construction_progress = self.get_construction_progress_by_id(id)
        self.repo.delete_construction_progress(construction_progress)

    def update_construction_progress(self, construction_progress: ConstructionProgress) -> None:
        self.repo.update_construction_progress(construction_progress)

    def get_construction_progress_for_construction_objects(self) -> ConstructionProgress:
        return self.repo.get_construction_progress_for_construction_objects()

    def convert_schema_to_object(self, schema: dict) -> ConstructionProgress:
        construction_progress = ConstructionProgress()
        if 'id' in schema:
            construction_progress.construction_progress_id = schema['id']

        construction_progress.construction_objects_id = schema['constructionObjects']
        construction_progress.reporting_date = schema['reportingDate']
        construction_progress.readiness = schema['readiness']
        construction_progress.people = schema['people']
        construction_progress.equipment = schema['equipment']
        # construction_progress.progress_statuses_id = schema['progressStatusesId']

        construction_progress.update_datetime = datetime.now()

        return construction_progress
