from .model import OKSM
from .repository import OKSMRepository


class OKSMService:

    def __init__(self):
        self.repo = OKSMRepository()

    def get_all_oksms(self) -> list:
        return self.repo.get_all_oksms()

    def get_oksm_by_id(self, id_: int) -> OKSM:
        return self.repo.get_oksm_by_id(id_)

    def add_oksm(self, oksm: OKSM) -> None:
        self.repo.add_oksm(oksm)

    def update_oksm(self, new_oksm: OKSM) -> None:
        self.repo.update_oksm(new_oksm)

    def delete_oksm_by_id(self, id_: int) -> None:
        self.repo.delete_oksm_by_id(id_)
