from mks_backend.repositories.organizations.organization import OrganisationRepository, Organization


class OrganisationService:

    def __init__(self):
        self.repo = OrganisationRepository()

    def get_processed_rootes(self, filter_params=None) -> list:
        if filter_params:
            if not self.get_reflect_disbanded(filter_params):
                return self.get_rootes_without_inactive()

        return self.get_rootes()

    def get_rootes_without_inactive(self) -> list:
        rootes = self.get_rootes()
        return self.filtered_organizations(rootes)

    def get_rootes(self) -> list:
        return self.repo.get_rootes()

    def filtered_organizations(self, organizations: list) -> list:
        return list(filter(lambda x: (x.is_active == True), organizations))

    def add_organization(self, organization: Organization) -> None:
        self.repo.add(organization)

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
        new_parent = self.repo.get_by_id(new_parent_uuid)

        new_parent.sub_organizations.extend(old_parent.sub_organizations)
        old_parent.sub_organizations.clear()

    def set_node_new_parent(self, organization_uuid: str, new_parent_uuid: str) -> None:
        """
        Set new parent for NODE in organization tree
        """
        organization = self.repo.get_by_id(organization_uuid)
        organization.parent_organizations_id = new_parent_uuid

        self.repo.update(organization)

    def get_by_id(self, organization_uuid: str) -> Organization:
        return self.repo.get_by_id(organization_uuid)

    def get_reflect_disbanded(self, params_deserialized: dict) -> bool:
        return params_deserialized.get('reflectDisbanded', True)
