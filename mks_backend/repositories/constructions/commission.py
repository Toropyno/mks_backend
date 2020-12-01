from mks_backend.models.constructions import Commission
from mks_backend.models import DBSession

from mks_backend.errors import DBBasicError, db_error_handler


class CommissionRepository:

    def __init__(self):
        self._query = DBSession.query(Commission)

    def get_all_commissions(self) -> list:
        return self._query.order_by(Commission.fullname).all()

    @db_error_handler
    def add_commission(self, commission: Commission) -> None:
        DBSession.add(commission)
        DBSession.commit()

    def delete_commission_by_id(self, id: int) -> None:
        commission = self.get_commission_by_id(id)
        if not commission.construction:
            DBSession.delete(commission)
            DBSession.commit()
        else:
            # case when some constructions use this commission
            raise DBBasicError('commission_limit')

    @db_error_handler
    def update_commission(self, commission: Commission) -> None:
        if DBSession.merge(commission) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('commission_ad')

    def get_commission_by_id(self, id: int) -> Commission:
        commission = self._query.get(id)
        if not commission:
            raise DBBasicError('commission_ad')
        return commission
