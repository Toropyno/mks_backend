from mks_backend.models.constructions import Commission
from mks_backend.repositories.constructions.commission import CommissionRepository

from mks_backend.errors.db_basic_error import db_error_handler


class CommissionService:

    def __init__(self):
        self.repo = CommissionRepository()

    def get_all_commissions(self) -> list:
        return self.repo.get_all_commissions()

    def get_commission_by_id(self, id: int) -> Commission:
        return self.repo.get_commission_by_id(id)

    @db_error_handler
    def add_commission(self, commission: Commission) -> None:
        self.repo.add_commission(commission)

    @db_error_handler
    def update_commission(self, new_commission: Commission) -> None:
        self.repo.update_commission(new_commission)

    def delete_commission_by_id(self, id: int) -> None:
        self.repo.delete_commission_by_id(id)
