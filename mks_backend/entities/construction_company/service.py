from .model import ConstructionCompany
from .repository import ConstructionCompanyRepository


class ConstructionCompanyService:

    def __init__(self):
        self.repo = ConstructionCompanyRepository()

    def get_all_construction_companies(self) -> list:
        return self.repo.get_all_construction_companies()

    def get_construction_company_by_id(self, id: int) -> ConstructionCompany:
        return self.repo.get_construction_company_by_id(id)

    def add_construction_company(self, construction_company: ConstructionCompany) -> None:
        self.repo.add_construction_company(construction_company)

    def update_construction_company(self, new_construction_company: ConstructionCompany) -> None:
        self.repo.update_construction_company(new_construction_company)

    def delete_construction_company_by_id(self, id: int) -> None:
        self.repo.delete_construction_company_by_id(id)
