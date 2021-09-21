from .repository import OrganisationRepository, Organization


class OrganizationService:

    def __init__(self):
        self.repo = OrganisationRepository()

    def get_rootes(self, reflect_disbanded: bool) -> list:
        rootes = self.repo.get_rootes()
        if reflect_disbanded is False:
            return self.get_active_rootes(rootes)
        return rootes

    def get_active_rootes(self, organizations: list) -> list:
        return list(filter(lambda org: org.is_active, organizations))

    def add_organization(self, organization: Organization) -> None:
        self.repo.add(organization)

    def update_organization(self, organization: Organization) -> None:
        self.repo.update(organization)

    def delete_organization(self, organization_uuid: str, new_parent_uuid: str = None) -> None:
        """
        Deletion can be done in two strategies: SOFT and HARD.
        SOFT: all children will get a new parent.
        HARD: all children of the node will be deleted.
        """
        if new_parent_uuid:
            self.set_children_new_parent(organization_uuid, new_parent_uuid)

        self.repo.delete(organization_uuid)

    def set_children_new_parent(self, old_parent_uuid: str, new_parent_uuid: str) -> None:
        """
        Set new parents for CHILDREN when organization removed by "soft" strategy
        """
        old_parent = self.repo.get_by_id(old_parent_uuid)

        if new_parent_uuid != 'null':
            new_parent = self.repo.get_by_id(new_parent_uuid)

            new_parent.sub_organizations.extend(old_parent.sub_organizations)
            old_parent.sub_organizations.clear()
        else:
            for children in old_parent.sub_organizations:
                children.parent_organizations_id = None

    def set_node_new_parent(self, organization_uuid: str, new_parent_uuid: str) -> None:
        """
        Set new parent for NODE in organization tree
        """
        organization = self.repo.get_by_id(organization_uuid)
        organization.parent_organizations_id = new_parent_uuid

        self.repo.update(organization)

    def get_by_id(self, organization_uuid: str) -> Organization:
        return self.repo.get_by_id(organization_uuid)
