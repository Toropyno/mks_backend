from mks_backend.models.zones import Zones
from mks_backend.repositories.zones_repository import ZoneRepository


class ZoneService:

    def __init__(self):
        self.repo = ZoneRepository()

    def get_all_zones(self) -> list:
        return self.repo.get_all_zones()

    def get_zone_by_id(self, id: int) -> Zones:
        return self.repo.get_zone_by_id(id)

    def add_zone(self, zone: Zones) -> None:
        self.repo.add_zone(zone)

    def delete_zone_by_id(self, id: int) -> None:
        self.repo.delete_zone_by_id(id)

    def update_zone(self, new_zone: Zones) -> None:
        self.repo.update_zone(new_zone)
