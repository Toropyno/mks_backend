from mks_backend.models.location import Location
from mks_backend.repositories import DBSession


class LocationRepository:

    @classmethod
    def add_location(cls, location: Location) -> None:
        DBSession.add(location)
        DBSession.commit()

    @classmethod
    def update_location(cls, location: Location) -> None:
        DBSession.query(Location).filter_by(id=location.id).update(
            {
                'longitude': location.longitude,
                'latitude': location.latitude,
                'zoom': location.zoom
            }
        )
        DBSession.commit()
