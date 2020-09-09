from mks_backend.models.construction import Construction
from mks_backend.repositories import DBSession
from mks_backend.errors.db_basic_error import db_error_handler


class ConstructionRepository:

    def get_all_constructions(self) -> list:
        return DBSession.query(Construction).order_by(Construction.contract_date).all()

    def get_construction_by_id(self, id: int) -> Construction:
        return DBSession.query(Construction).get(id)


    def add_construction(self, construction: Construction) -> None:
        DBSession.add(construction)
        DBSession.commit()

    @db_error_handler
    def update_construction(self, construction: Construction) -> None:
        DBSession.query(Construction).filter_by(construction_id=construction.construction_id).update(
            {
                'project_code': construction.project_code,
                'project_name': construction.project_name,
                'construction_categories_id': construction.construction_categories_id,
                'subcategories_list_id': construction.subcategories_list_id,
                'is_critical': construction.is_critical,
                'commission_id': construction.commission_id,
                'idMU': construction.idMU,
                'contract_date': construction.contract_date,
                'object_amount': construction.object_amount,
                'planned_date': construction.planned_date
            }
        )
        DBSession.commit()

    def delete_construction(self, id: int) -> None:
        construction = self.get_construction_by_id(id)
        DBSession.delete(construction)
        DBSession.commit()

    def filter_constructions(self, params: dict) -> list:
        constructions = DBSession.query(Construction)

        if 'project_code' in params:
            project_code = params['project_code']
            constructions = constructions.filter(Construction.project_code.ilike('%{}%'.format(project_code)))
        if 'project_name' in params:
            projet_name = params['project_name']
            constructions = constructions.filter(Construction.project_name.ilike('%{}%'.format(projet_name)))
        if 'constructions_categories_id' in params:
            category_id = params['constructions_categories_id']
            constructions = constructions.filter(Construction.construction_categories_id == category_id)
        if 'subcategories_list_id' in params:
            subcategories_list_id = params['subcategories_list_id']
            constructions = constructions.filter(Construction.subcategories_list_id == subcategories_list_id)
        if 'is_critical' in params:
            is_critical = params['is_critical']
            constructions = constructions.filter(Construction.is_critical == is_critical)
        if 'commission_id' in params:
            commission_id = params['commission_id']
            constructions = constructions.filter(Construction.commission_id == commission_id)
        if 'idMU' in params:
            idMU = params['idMU']
            constructions = constructions.filter(Construction.idMU == idMU)
        if 'object_amount' in params:
            object_amount = params['object_amount']
            constructions = constructions.filter(Construction.object_amount == object_amount)
        if 'contract_date_start' in params:
            contract_date_start = params['contract_date_start']
            constructions = constructions.filter(Construction.contract_date >= contract_date_start)
        if 'contract_date_end' in params:
            contract_date_end = params['contract_date_end']
            constructions = constructions.filter(Construction.contract_date <= contract_date_end)
        if 'planned_date_start' in params:
            planned_date_start = params['planned_date_start']
            constructions = constructions.filter(Construction.planned_date >= planned_date_start)
        if 'planned_date_end' in params:
            planned_date_end = params['planned_date_end']
            constructions = constructions.filter(Construction.planned_date <= planned_date_end)

        return constructions.order_by(Construction.contract_date).all()
