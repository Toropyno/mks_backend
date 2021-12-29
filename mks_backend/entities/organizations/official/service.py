from typing import List

from .model import Official
from .repository import OfficialRepository

from mks_backend.entities.organizations.organization import OrganizationService


class OfficialService:

    def __init__(self):
        self.repo = OfficialRepository()
        self.organization_service = OrganizationService()

    def add_official(self, official: Official) -> None:
        self.repo.add_official(official)

    def update_official(self, official: Official) -> None:
        self.repo.update_official(official)

    def delete_official_by_id(self, id_: int) -> None:
        self.repo.delete_official(id_)

    def get_officials_by_organization(self, filter_fields: dict) -> List[Official]:
        return self.repo.get_officials_by_organization(filter_fields)

    def get_official(self, id_: int) -> Official:
        return self.repo.get_official(id_)
