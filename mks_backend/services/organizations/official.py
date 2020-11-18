from mks_backend.models.organizations.official import Official
from mks_backend.repositories.organizations.official import OfficialRepository
from mks_backend.services.organizations.organization import OrganisationService


class OfficialService:

    def __init__(self):
        self.repo = OfficialRepository()
        self.organization_service = OrganisationService()

    def add_official(self, official: Official) -> None:
        self.repo.add_official(official)

    def update_official(self, official: Official) -> None:
        self.repo.update_official(official)

    def delete_official_by_id(self, id: int) -> None:
        self.repo.delete_official(id)

    def get_officials_by_organization(self, organization_uuid: str, reflect_vacated_position: bool) -> list:
        officials = self.organization_service.get_by_id(organization_uuid).officials

        if reflect_vacated_position is False:
            officials = self.get_filtered_officials(officials)
        return officials

    def get_filtered_officials(self, officials: list) -> list:
        return list(filter(lambda ofl: ofl.end_date is None, officials))
