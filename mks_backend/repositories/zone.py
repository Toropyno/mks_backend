from mks_backend.models.zone import Zone
from mks_backend.repositories import DBSession
from mks_backend.errors.db_basic_error import db_error_handler


class ZoneRepository:

    def get_zone_by_id(self, id: int) -> Zone:
        return DBSession.query(Zone).get(id)

    def get_all_zones(self) -> list:
        return DBSession.query(Zone).all()

    @db_error_handler
    def add_zone(self, zone: Zone) -> None:
        DBSession.add(zone)
        DBSession.commit()

    def delete_zone_by_id(self, id: int) -> None:
        zone = self.get_zone_by_id(id)
        DBSession.delete(zone)
        DBSession.commit()

    @db_error_handler
    def update_zone(self, zone: Zone) -> None:
        DBSession.query(Zone).filter_by(zones_id=zone.zones_id).update(
            {
                'fullname': zone.fullname
            }
        )
        DBSession.commit()
