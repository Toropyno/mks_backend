from mks_backend.models.commission import Commission
from mks_backend.repositories import DBSession


class CommissionRepository:

    def get_all_commissions(self) -> list:
        return DBSession.query(Commission).order_by(Commission.fullname).all()

    def add_commission(self, commission: Commission) -> None:
        DBSession.add(commission)
        DBSession.commit()

    def delete_commission_by_id(self, id: int) -> None:
        commission = self.get_commission_by_id(id)
        DBSession.delete(commission)
        DBSession.commit()

    def update_commission(self, commission: Commission) -> None:
        DBSession.query(Commission).filter_by(commission_id=commission.commission_id).update(
            {
                'fullname': commission.fullname,
                'code': commission.code
            }
        )

        DBSession.commit()

    def get_commission_by_id(self, id: int) -> Commission:
        return DBSession.query(Commission).get(id)
