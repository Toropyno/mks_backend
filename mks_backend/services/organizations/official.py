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

    def get_officials_by_organization(self, organization_uuid: str, filter_params=None) -> list:
        officials = self.organization_service.get_by_id(organization_uuid).officials

        if filter_params:
            if not self.get_reflect_vacated_position(filter_params):
                officials = list(filter(lambda x: x.end_date == None, officials))

        return officials

    def get_reflect_vacated_position(self, params_deserialized: dict) -> bool:
        return params_deserialized.get('reflectVacatedPosition', True)
