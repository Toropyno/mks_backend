from .model import Litigation
from .repository import LitigationRepository


class LitigationService:

    def __init__(self):
        self.repo = LitigationRepository()

    def get_all_litigations(self) -> list:
        return self.repo.get_all_litigations()

    def get_litigation_by_id(self, id_: int) -> Litigation:
        return self.repo.get_litigation_by_id(id_)

    def add_litigation(self, litigation) -> None:
        self.repo.add_litigation(litigation)

    def update_litigation(self, new_litigation) -> None:
        self.repo.update_litigation(new_litigation)

    def delete_litigation_by_id(self, id_: int) -> None:
        self.repo.delete_litigation_by_id(id_)
