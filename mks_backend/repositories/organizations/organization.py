from typing import List

from mks_backend.models.organizations.organization import Organization
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import DBBasicError


class OrganisationRepository:

    def __init__(self):
        self._query = DBSession.query(Organization)

    def add(self, organization: Organization):
        DBSession.add(organization)
        DBSession.commit()

    def update(self, organization: Organization):
        if DBSession.merge(organization) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('organization_ad')

    def get_by_id(self, uuid: str) -> Organization:
        organization = self._query.get(uuid)
        if not organization:
            raise DBBasicError('organization_nf')
        return organization

    def delete(self, organization_uuid: str):
        self._query.filter(Organization.organizations_id == organization_uuid).delete()
        DBSession.commit()

    def get_rootes(self) -> List[Organization]:
        DBSession.commit()
        rootes = self._query.filter(Organization.parent_organizations_id == None).all()
        return sorted(rootes, key=lambda root: root.shortname)
