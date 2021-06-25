from mks_backend import DBSession
from mks_backend.errors import DBBasicError
from mks_backend.models.geoobject.geo_style import GeoStyle


class GeoStyleRepository:
    def __init__(self):
        self._query = DBSession.query(GeoStyle)

    def get_geo_style_by_id(self, id: int) -> GeoStyle:
        style = self._query.get(id)
        if not style:
            raise DBBasicError('protocol_ad')
        return style