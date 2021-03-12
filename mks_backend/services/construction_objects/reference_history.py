from typing import List

from mks_backend.models.construction_objects.reference_history import ReferenceHistory
from mks_backend.repositories.construction_objects.reference_history import ReferenceHistoryRepository


class ReferenceHistoryService:

    def __init__(self):
        self.repo = ReferenceHistoryRepository()

    def get_reference_history_by_construction_object_id(self, construction_object_id: int) -> List[ReferenceHistory]:
        return self.repo.get_reference_history_by_construction_object_id(construction_object_id)
