from mks_backend.models.construction import Construction
from mks_backend.repositories import DBSession


class ConstructionRepository:

    @classmethod
    def get_construction_by_id(cls, id):
        return DBSession.query(Construction).get(id)

    def get_all_construction(self):
        return DBSession.query(Construction).all()

    def add_construction(self, construction):
        DBSession.add(construction)
        DBSession.commit()

    def update_construction(self, construction):
        DBSession.query(Construction).filter_by(construction_id=construction.construction_id).update(
            {'project_code': construction.project_code,
             'project_name': construction.project_name,
             'construction_categories_id': construction.construction_categories_id,
             'subcategories_list_id': construction.subcategories_list_id,
             'is_critical': construction.is_critical,
             'commission_id': construction.commission_id,
             'idMU': construction.idMU,
             'contract_date': construction.contract_date,
             'object_amount': construction.object_amount,
             'planned_date': construction.planned_date
            })
        DBSession.commit()

    def delete_construction(self, id):
        construction = self.get_construction_by_id(id)
        DBSession.delete(construction)
        DBSession.commit()

    def filter_construction(self, params):
        constructions = DBSession.query(Construction)
        # add filters from params
        return constructions.all()
