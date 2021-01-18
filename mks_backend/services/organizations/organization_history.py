from mks_backend.services.organizations.organization import OrganisationService
from mks_backend.models.organizations.organization_history import OrganizationHistory
from mks_backend.repositories.organizations.organization_history import OrganizationHistoryRepository


class OrganizationHistoryService:

    def __init__(self):
        self.organization_service = OrganisationService()
        self.repo = OrganizationHistoryRepository()

    def add_organization_history(self, organization_history: OrganizationHistory):
        self.repo.add(organization_history)

    def get_organization_history_by_organization_uuid(self, organization_uuid: str) -> list:
        return self.repo.get_history_by_organization_uuid(organization_uuid)

    def update_organization_history(self, organization_history: OrganizationHistory):
        self.repo.update(organization_history)

    def delete_organization_history(self, organization_history_id: int):
        self.repo.delete(organization_history_id)
