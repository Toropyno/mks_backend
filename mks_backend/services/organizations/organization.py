from mks_backend.repositories.organizations.organization import OrganisationRepository, Organization


class OrganisationService:

    def __init__(self):
        self.repo = OrganisationRepository()

    def get_rootes(self):
        return self.repo.get_rootes()

    def add_organization(self, organization: Organization) -> None:
        self.repo.add(organization)

    def delete_organization(self, organization_uuid: str, new_parent_uuid=None) -> None:
        if new_parent_uuid:
            self.set_children_new_parent(organization_uuid, new_parent_uuid)

        self.repo.delete(organization_uuid)

    def set_children_new_parent(self, old_parent_uuid: str, new_parent_uuid: str) -> None:
        """
        Set new parents for CHILDREN when organization removed by "soft" strategy
        """
        old_parent = self.repo.get(old_parent_uuid)
        new_parent = self.repo.get(new_parent_uuid)

        new_parent.sub_organizations.extend(old_parent.sub_organizations)
        old_parent.sub_organizations.clear()

    def set_node_new_parent(self, organization_uuid: str, new_parent_uuid: str) -> None:
        """
        Set new parent for NODE in organization tree
        """
        organization = self.repo.get(organization_uuid)
        organization.parent_organizations_id = new_parent_uuid

        self.repo.update()
