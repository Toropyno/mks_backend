from typing import List, Tuple

from mks_backend.entities.constructions.construction import Construction
from mks_backend.entities.litigation_work.litigation.service import LitigationService

from .model import LitigationSubject
from .repository import LitigationSubjectRepository


class LitigationSubjectService:

    def __init__(self):
        self.litigation_service = LitigationService()
        self.repo = LitigationSubjectRepository()

    def get_litigation_subjects_by_litigation(self, litigation_id: int) -> List[Construction]:
        return self.litigation_service.get_litigation_by_id(litigation_id).constructions

    def delete_litigation_subject(self, litigation_id: int, construction_id: int) -> None:
        self.repo.delete_litigation_subject(litigation_id, construction_id)

    def add_litigation_subjects(self, litigation_subjects: Tuple[LitigationSubject]):
        self.repo.add_litigation_subjects(litigation_subjects)
