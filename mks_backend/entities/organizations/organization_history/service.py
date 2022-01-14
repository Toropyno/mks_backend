from mks_backend.entities.organizations.organization import OrganizationService
from mks_backend.errors import BusinessLogicError

from .model import OrganizationHistory
from .repository import OrganizationHistoryRepository


class OrganizationHistoryService:

    def __init__(self):
        self.organization_service = OrganizationService()
        self.repo = OrganizationHistoryRepository()

    def add_organization_history(self, organization_history: OrganizationHistory) -> None:
        self.check_org_sign_details(organization_history)
        self.repo.add(organization_history)

    def update_organization_history(self, organization_history: OrganizationHistory) -> None:
        self.check_org_sign_details(organization_history)
        self.repo.update(organization_history)

    def check_org_sign_details(self, organization_history: OrganizationHistory) -> None:
        organization = self.organization_service.get_by_id(organization_history.organizations_id)
        if organization.org_sign:
            if not all([organization_history.inn, organization_history.kpp, organization_history.ogrn]):
                raise BusinessLogicError('no_details')

    def get_organization_history_by_organization_uuid(self, organization_uuid: str) -> list:
        return self.repo.get_history_by_organization_uuid(organization_uuid)

    def delete_organization_history(self, organization_history_id: int):
        self.repo.delete(organization_history_id)
