from mks_backend.models.zone import Zone
from mks_backend.models import DBSession

from mks_backend.errors import db_error_handler, DBBasicError


class ZoneRepository:

    def __init__(self):
        self._query = DBSession.query(Zone)

    def get_zone_by_id(self, id: int) -> Zone:
        return self._query.get(id)

    def get_all_zones(self) -> list:
        return self._query.order_by(Zone.fullname).all()

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
        if DBSession.merge(zone) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('zone_ad')
