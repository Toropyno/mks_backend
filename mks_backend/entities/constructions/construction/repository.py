from .model import Construction

from mks_backend.entities.fias import FIAS

from mks_backend.session import DBSession
from mks_backend.errors import DBBasicError


class ConstructionRepository:

    def __init__(self):
        self._query = DBSession.query(Construction)

    def get_all_constructions(self) -> list:
        return self._query.order_by(Construction.project_code).all()

    def get_construction_by_id(self, id_: int) -> Construction:
        construction = self._query.get(id_)
        if not construction:
            raise DBBasicError('construction_nf')
        return construction

    def add_construction(self, construction: Construction) -> None:
        DBSession.add(construction)
        DBSession.commit()

    def update_construction(self, construction: Construction) -> None:
        if DBSession.merge(construction):  # TODO: add new condition when FIAS will be ok
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_ad')

    def delete_construction(self, id: int) -> None:
        construction = self.get_construction_by_id(id)
        DBSession.delete(construction)
        DBSession.commit()

    def filter_constructions(self, params: dict) -> list:
        constructions = self._query.outerjoin(FIAS)

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
        if 'construction_types_id' in params:
            types_id = params['construction_types_id']
            constructions = constructions.filter(Construction.construction_types_id == types_id)
        if 'construction_companies_id' in params:
            companies_id = params['construction_companies_id']
            constructions = constructions.filter(Construction.construction_companies_id == companies_id)
        if 'location_types_id' in params:
            location_types_id = params['location_types_id']
            constructions = constructions.filter(Construction.location_types_id == location_types_id)
        if 'oksm_id' in params:
            oksm_id = params['oksm_id']
            constructions = constructions.filter(Construction.oksm_id == oksm_id)
        if 'address' in params:
            address = params['address']
            constructions = constructions.filter(Construction.address_full == address)
        if 'region' in params:
            region = '%' + params['region'] + '%'
            constructions = constructions.filter(FIAS.region.ilike(region))
        if 'area' in params:
            region = '%' + params['area'] + '%'
            constructions = constructions.filter(FIAS.area.ilike(region))
        if 'city' in params:
            region = '%' + params['city'] + '%'
            constructions = constructions.filter(FIAS.city.ilike(region))
        if 'settlement' in params:
            region = '%' + params['settlement'] + '%'
            constructions = constructions.filter(FIAS.settlement.ilike(region))
        if 'organization' in params:
            constructions = constructions.filter(Construction.organizations_id == params['organization'])
        if 'military_district' in params:
            constructions = constructions.filter(Construction.military_district_id == params['military_district'])
        if 'deletion_mark' in params:
            constructions = constructions.filter(Construction.deletion_mark)

        # TODO: filter planned date start/end, filter readiness

        return constructions.order_by(Construction.project_code).all()
