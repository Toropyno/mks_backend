from mks_backend.models.commission import Commission
from mks_backend.repositories import DBSession


class CommissionRepository:

    @classmethod
    def get_commission_by_id(cls, id):
        return DBSession.query(Commission).get(id)

    def get_all_commission(self):
        return DBSession.query(Commission).all()

    def add_commission(self, commission):
        DBSession.add(commission)
        DBSession.commit()

    def delete_commission_by_id(self, id):
        commission = self.get_commission_by_id(id)
        DBSession.delete(commission)
        DBSession.commit()

    def updete_commission(self, commission):
        DBSession.query(Commission).filter_by(commission_id=commission.commission_id).update(
            {'fullname': commission.fullname,
            'code': commission.code})
        DBSession.commit()

