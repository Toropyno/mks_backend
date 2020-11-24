from mks_backend.models import DBSession
from mks_backend.models.organizations.organization_history import OrganizationHistory

from mks_backend.errors.db_basic_error import db_error_handler, DBBasicError


class OrganizationHistoryRepository:

    def __init__(self):
        self._query = DBSession.query(OrganizationHistory)

    @db_error_handler
    def add(self, organization_history: OrganizationHistory) -> None:
        DBSession.add(organization_history)
        DBSession.commit()

    @db_error_handler
    def update(self, organization_history: OrganizationHistory) -> None:
        DBSession.merge(organization_history)
        DBSession.commit()

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
