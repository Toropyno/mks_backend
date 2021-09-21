from typing import List

from .model import ObjectCompletion
from .repository import ObjectCompletionRepository


class ObjectCompletionService:

    def __init__(self):
        self.repo = ObjectCompletionRepository()

    def get_object_completion_by_construction_object_id(self, construction_object_id: int) -> List[ObjectCompletion]:
        return self.repo.get_object_completion_by_construction_object_id(construction_object_id)
