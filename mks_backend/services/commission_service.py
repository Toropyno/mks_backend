from mks_backend.repositories.commission_repository import CommissionRepository
from mks_backend.errors.db_basic_error import db_error_handler


class CommissionService:
    def __init__(self):
        self.repo = CommissionRepository()

    def get_all_commissions(self):
        return self.repo.get_all_commissions()

    def get_commission_by_id(self, id):
        return self.repo.get_commission_by_id(id)

    @db_error_handler
    def add_commission(self, commission):
        self.repo.add_commission(commission)

    @db_error_handler
    def update_commission(self, new_commission):
        self.repo.update_commission(new_commission)

    def delete_commission_by_id(self, id):
        self.repo.delete_commission_by_id(id)
