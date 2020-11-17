from typing import List

from mks_backend.models.organizations.organization import Organization
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import DBBasicError, db_error_handler


class OrganisationRepository:

    def __init__(self):
        self._query = DBSession.query(Organization)

    @db_error_handler
    def add(self, organization: Organization):
        DBSession.add(organization)
        DBSession.commit()

    @db_error_handler
    def update(self, organization: Organization):
        DBSession.merge(organization)
        DBSession.commit()

    def get_by_id(self, uuid: str) -> Organization:
        organization = self._query.get(uuid)
        if not organization:
            raise DBBasicError('organization_nf')
        return organization

    def delete(self, organization_uuid: str):
        organization = self.get_by_id(organization_uuid)
        DBSession.delete(organization)

    def get_rootes(self) -> List[Organization]:
        rootes = self._query.filter(Organization.parent_organizations_id == None).all()
        return sorted(rootes, key=lambda root: root.shortname)
