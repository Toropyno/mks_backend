from typing import List

from .model import Litigation
from .repository import LitigationRepository


class LitigationService:

    def __init__(self):
        self.repo = LitigationRepository()

    def get_litigation_by_id(self, id_: int) -> Litigation:
        return self.repo.get_litigation_by_id(id_)

    def add_litigation(self, litigation) -> None:
        self.repo.add_litigation(litigation)

    def update_litigation(self, litigation) -> None:
        self.repo.update_litigation(litigation)

    def delete_litigation_by_id(self, id_: int) -> None:
        self.repo.delete_litigation_by_id(id_)

    def get_litigations(self, filter_params: dict = None) -> List[Litigation]:
        return self.repo.get_litigations(filter_params)
