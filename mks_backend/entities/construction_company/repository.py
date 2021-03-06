from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import ConstructionCompany


class ConstructionCompanyRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionCompany)

    def get_all_construction_companies(self) -> list:
        return self._query.order_by(ConstructionCompany.fullname).all()

    def add_construction_company(self, construction_company: ConstructionCompany) -> None:
        DBSession.add(construction_company)
        DBSession.commit()

    def delete_construction_company_by_id(self, id_: int) -> None:
        self._query.filter(ConstructionCompany.construction_companies_id == id_).delete()
        DBSession.commit()

    def update_construction_company(self, new_construction_company: ConstructionCompany) -> None:
        if DBSession.merge(new_construction_company) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_company_ad')

    def get_construction_company_by_id(self, id_: int) -> ConstructionCompany:
        return self._query.get(id_)
