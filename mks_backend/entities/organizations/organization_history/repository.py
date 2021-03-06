from sqlalchemy import desc

from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import OrganizationHistory


class OrganizationHistoryRepository:

    def __init__(self):
        self._query = DBSession.query(OrganizationHistory)

    def add(self, organization_history: OrganizationHistory) -> None:
        DBSession.add(organization_history)
        DBSession.commit()

    def update(self, organization_history: OrganizationHistory) -> None:
        if DBSession.merge(organization_history) and not DBSession.new:
            if any([
                organization_history.address_legal, organization_history.inn,
                organization_history.kpp, organization_history.ogrn
            ]) and not self.get(organization_history.organizations_history_id).organization.org_sign:
                DBSession.rollback()
                raise DBBasicError('organization_not_legal_logical')
            else:
                DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('organization_history_ad')

    def delete(self, id_: int) -> None:
        organization_history = self.get(id_)

        if len(organization_history.organization.history) == 1:
            raise DBBasicError('organization_history_delete_limit')

        DBSession.delete(organization_history)
        DBSession.commit()

    def get(self, id_: int) -> OrganizationHistory:
        organization_history = self._query.get(id_)
        if not organization_history:
            raise DBBasicError('organization_history_nf')
        return organization_history

    def get_history_by_organization_uuid(self, organization_uuid):
        DBSession.commit()
        history = self._query.filter(OrganizationHistory.organizations_id == organization_uuid).\
            order_by(desc(OrganizationHistory.begin_date)).all()
        return history
