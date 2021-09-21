from .model import OrganizationHistory
from .repository import OrganizationHistoryRepository

from mks_backend.entities.organizations.organization import OrganizationService


class OrganizationHistoryService:

    def __init__(self):
        self.organization_service = OrganizationService()
        self.repo = OrganizationHistoryRepository()

    def add_organization_history(self, organization_history: OrganizationHistory):
        self.repo.add(organization_history)

    def get_organization_history_by_organization_uuid(self, organization_uuid: str) -> list:
        return self.repo.get_history_by_organization_uuid(organization_uuid)

    def update_organization_history(self, organization_history: OrganizationHistory):
        self.repo.update(organization_history)

    def delete_organization_history(self, organization_history_id: int):
        self.repo.delete(organization_history_id)
