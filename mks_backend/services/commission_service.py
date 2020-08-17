from mks_backend.repositories.commission_repository import CommissionRepository
from mks_backend.models.commission import Commission


class CommissionService:
    def __init__(self):
        self.repo = CommissionRepository()

    def get_all_commissions(self):
        return self.repo.get_all_commissions()

    def get_commission_by_id(self, id):
        return self.repo.get_commission_by_id(id)

    def add_commission(self, commission):
        if self.repo.get_commission_by_code(commission.code):
            raise ValueError('Комиссия с таким кодом уже существует')
        elif self.repo.get_commission_by_fullname(commission.fullname):
            raise ValueError('Комиссия с таким именем уже существует')

        self.repo.add_commission(commission)

    def update_commission(self, new_commission):
        old_commission = self.repo.get_commission_by_id(new_commission.commission_id)

        if old_commission.code != new_commission.code:
            if self.repo.get_commission_by_code(new_commission.code):
                raise ValueError('Коммиссия с таким кодом уже существует')
        if old_commission.fullname != new_commission.fullname:
            if self.repo.get_commission_by_fullname(new_commission.fullname):
                raise ValueError('Коммиссия с таким именем уже существует')

        self.repo.update_commission(new_commission)

    def delete_commission_by_id(self, id):
        self.repo.delete_commission_by_id(id)

    def convert_schema_to_object(self, schema):
        commission = Commission()

        commission.commission_id = schema.get('id')
        commission.code = schema.get('code')
        commission.fullname = schema.get('fullName')

        return commission

