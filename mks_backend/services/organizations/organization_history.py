from mks_backend.models.organizations.organization_history import OrganizationHistory
from mks_backend.repositories.organizations.organization_history import OrganizationHistoryRepository


class OrganizationHistoryService:

    def __init__(self):
        self.repo = OrganizationHistoryRepository()

    def add_organization_history(self, organization_history: OrganizationHistory):
        self.repo.add(organization_history)

    def update_organization_history(self, organization_history: OrganizationHistory):
        self.repo.update(organization_history)

    def delete_organization_history(self, organization_history_id: int):
        self.repo.delete(organization_history_id)
