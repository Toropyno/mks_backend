from mks_backend.models.geoobject.geo_style import GeoStyle
from mks_backend.repositories.geoobject.geo_style import GeoStyleRepository


class GeoStyleService:

    def __init__(self):
        self.repo = GeoStyleRepository()

    def get_geo_style_by_id(self, id: int) -> GeoStyle:
        return self.repo.get_geo_style_by_id(id)
