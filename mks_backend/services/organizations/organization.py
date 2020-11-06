from mks_backend.repositories.organizations.organization import OrganisationRepository, Organization


class OrganisationService:

    def __init__(self):
        self.repo = OrganisationRepository()

    def get_rootes(self):
        return self.repo.get_rootes()

    def delete_organization(self, organization_uuid: str, new_parent_uuid=None) -> None:
        if new_parent_uuid:
            self.set_new_parent(organization_uuid, new_parent_uuid)

        self.repo.delete_organization(organization_uuid)

    def set_new_parent(self, old_parent_uuid: str, new_parent_uuid: str) -> None:
        old_parent = self.repo.get_organization(old_parent_uuid)
        new_parent = self.repo.get_organization(new_parent_uuid)

        new_parent.sub_organizations.extend(old_parent.sub_organizations)
        old_parent.sub_organizations.clear()

    def add_organization(self, organization: Organization) -> None:
        self.repo.add_organization(organization)
