from .model import Commission
from .repository import CommissionRepository


class CommissionService:

    def __init__(self):
        self.repo = CommissionRepository()

    def get_all_commissions(self) -> list:
        return self.repo.get_all_commissions()

    def get_commission_by_id(self, id_: int) -> Commission:
        return self.repo.get_commission_by_id(id_)

    def add_commission(self, commission: Commission) -> None:
        self.repo.add_commission(commission)

    def update_commission(self, new_commission: Commission) -> None:
        self.repo.update_commission(new_commission)

    def delete_commission_by_id(self, id_: int) -> None:
        self.repo.delete_commission_by_id(id_)
