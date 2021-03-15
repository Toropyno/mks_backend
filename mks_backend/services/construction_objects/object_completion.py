from typing import List

from mks_backend.models.construction_objects.object_completion import ObjectCompletion
from mks_backend.repositories.construction_objects.object_completion import ObjectCompletionRepository


class ObjectCompletionService:

    def __init__(self):
        self.repo = ObjectCompletionRepository()

    def get_object_completion_by_construction_object_id(self, construction_object_id: int) -> List[ObjectCompletion]:
        return self.repo.get_object_completion_by_construction_object_id(construction_object_id)
