from typing import List

from mks_backend.models.organizations.organization import Organization
from mks_backend.repositories import DBSession


class OrganisationRepository:

    def __init__(self):
        self._query = DBSession.query(Organization)

    def get_rootes(self) -> List[Organization]:
        rootes = self._query.filter(Organization.parent_organizations_id == None).all()
        return sorted(rootes, key=lambda root: root.shortname)

    def get_organization(self, uuid: str) -> Organization:
        return self._query.get(uuid)

    def delete_organization(self, organization_uuid: str):
        self._query.filter(Organization.organizations_id == organization_uuid).delete()
        DBSession.commit()

    def add_organization(self, organization: Organization):
        DBSession.add(organization)
        DBSession.commit()
