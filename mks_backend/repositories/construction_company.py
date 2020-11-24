from mks_backend.models.construction_company import ConstructionCompany
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class ConstructionCompanyRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionCompany)

    def get_all_construction_companies(self) -> list:
        return self._query.order_by(ConstructionCompany.fullname).all()

    @db_error_handler
    def add_construction_company(self, construction_company: ConstructionCompany) -> None:
        DBSession.add(construction_company)
        DBSession.commit()

    def delete_construction_company_by_id(self, id: int) -> None:
        self._query.filter(ConstructionCompany.construction_companies_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_construction_company(self, new_construction_company: ConstructionCompany) -> None:
        DBSession.merge(new_construction_company)
        DBSession.commit()

    def get_construction_company_by_id(self, id: int) -> ConstructionCompany:
        return self._query.get(id)
