from mks_backend.models.zone import Zone
from mks_backend.repositories.zone import ZoneRepository


class ZoneService:

    def __init__(self):
        self.repo = ZoneRepository()

    def get_all_zones(self) -> list:
        return self.repo.get_all_zones()

    def get_zone_by_id(self, id: int) -> Zone:
        return self.repo.get_zone_by_id(id)

    def add_zone(self, zone: Zone) -> None:
        self.repo.add_zone(zone)

    def delete_zone_by_id(self, id: int) -> None:
        self.repo.delete_zone_by_id(id)

    def update_zone(self, new_zone: Zone) -> None:
        self.repo.update_zone(new_zone)
