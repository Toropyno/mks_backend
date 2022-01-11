from .model import Zone
from .repository import ZoneRepository

from mks_backend.entities.construction_objects.object_category import ObjectCategoryService


class ZoneService:

    def __init__(self):
        self.repo = ZoneRepository()
        self.object_categories_service = ObjectCategoryService()

    def get_all_zones(self) -> list:
        return self.repo.get_all_zones()

    def get_zone_by_id(self, id_: int) -> Zone:
        return self.repo.get_zone_by_id(id_)

    def add_zone(self, zone: Zone) -> None:
        self.repo.add_zone(zone)

    def delete_zone_by_id(self, id_: int) -> None:
        self.repo.delete_zone_by_id(id_)

    def update_zone(self, new_zone: Zone) -> None:
        self.repo.update_zone(new_zone)

    def to_mapped_object(self, schema: dict) -> Zone:
        zone_id = schema.get('id')
        if zone_id:
            zone = self.get_zone_by_id(zone_id)
        else:
            zone = Zone()

        categories = schema.get('categories', [])
        if categories is not None:
            categories_ids = list(map(lambda x: x['id'], categories))
            zone.object_categories = self.object_categories_service.get_many_object_categories_by_id(
                categories_ids
            )

        zone.fullname = schema.get('fullName')
        return zone
