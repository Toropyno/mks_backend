from mks_backend.models.fias import FIAS
from mks_backend.repositories import DBSession


class FIASRepository:

    def add_fias(self, fias: FIAS) -> None:
        DBSession.add(fias)
        DBSession.commit()

    def get_fias_by_id(self, id: int) -> FIAS:
        return DBSession.query(FIAS).get(id)

    def delete_fias_by_id(self, id: int) -> None:
        fias = self.get_fias_by_id(id)
        DBSession.delete(fias)
        DBSession.commit()

    def update_fias(self, fias: FIAS) -> None:
        DBSession.query(FIAS).filter_by(id=fias.id).update(
            {
                'subject': fias.subject,
                'district': fias.district,
                'city': fias.city,
                'locality': fias.locality,
                'remaining_address': fias.remaining_address
            }
        )
        DBSession.commit()

    def get_all_fiases(self) -> list:
        return DBSession.query(FIAS).all()


