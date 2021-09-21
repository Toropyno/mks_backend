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

    def delete_official_by_id(self, id: int) -> None:
        self.repo.delete_official(id)

    def get_officials_by_organization(self, organization_uuid: str, reflect_vacated_position: bool) -> list:
        officials = self.organization_service.get_by_id(organization_uuid).officials

        if reflect_vacated_position is False:
            officials = self.get_active_officials(officials)
        return officials

    def get_active_officials(self, officials: list) -> list:
        return list(filter(lambda ofl: not ofl.end_date, officials))

    def get_official(self, id_: int):
        return self.repo.get_official(id_)
