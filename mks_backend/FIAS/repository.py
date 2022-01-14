from mks_backend.session import DBSession

from .model import FIAS


class FIASrepo:

    def __init__(self):
        self._query = DBSession.query(FIAS)

    def get_fias_by_id(self, id_: int) -> FIAS:
        return self._query.get(id_)

    def get_fias_by_aoid(self, aoid):
        return self._query.filter(FIAS.aoid == aoid).first()

    def get_all_fiases(self) -> list:
        return self._query.all()

    def add_fias(self, fias: FIAS) -> None:
        DBSession.add(fias)
        DBSession.commit()

    def delete_fias_by_id(self, id_: int) -> None:
        fias = self.get_fias_by_id(id_)
        DBSession.delete(fias)
        DBSession.commit()

    def get_distincts(self, field):
        """
        good: [('край Приморский',), ('обл Оренбургская',), ('обл Тульская',)]
        bad: [(None,)]
        """
        distincts_values = DBSession.query(field).distinct(field).order_by(field)
        return [value[0] for value in distincts_values] if distincts_values[0][0] else None
