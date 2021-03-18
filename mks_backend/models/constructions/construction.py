from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    VARCHAR,
    Boolean,
    DATE,
    CheckConstraint,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mks_backend.session import Base
from mks_backend.db_schemas import ORGANIZATION_SCHEMA, MU_SCHEMA


class Construction(Base):
    __tablename__ = 'construction'

    construction_id = Column(Integer, primary_key=True, autoincrement=True)
    project_code = Column(VARCHAR(40), unique=True, nullable=False)
    project_name = Column(VARCHAR(255), nullable=False)
    is_critical = Column(Boolean, nullable=False)
    address_full = Column(VARCHAR(1000))
    note = Column(VARCHAR(1000))
    department = Column(VARCHAR(255))
    officer = Column(VARCHAR(100))
    technical_spec = Column(Boolean, nullable=False, default=False)
    price_calc = Column(Boolean, nullable=False, default=False)
    deletion_mark = Column(Boolean, nullable=False, default=False)

    construction_categories_id = Column(
        Integer,
        ForeignKey('construction_categories.construction_categories_id', ondelete='SET NULL')
    )

    subcategories_list_id = Column(
        Integer,
        ForeignKey('subcategories_list.subcategories_list_id', ondelete='SET NULL')
    )

    commission_id = Column(
        Integer,
        ForeignKey('commission.commission_id'),
        nullable=False
    )

    idMU = Column(
        Integer,
        ForeignKey('{schema}.military_unit.idMU'.format(schema=MU_SCHEMA)),
    )

    military_district_id = Column(
        Integer,
        ForeignKey('{schema}.military_unit.idMU'.format(schema=MU_SCHEMA)),
        nullable=False
    )

    object_amount = Column(
        Integer,
        CheckConstraint('object_amount>0'),
        nullable=False
    )

    construction_types_id = Column(
        Integer,
        ForeignKey('construction_types.construction_types_id', ondelete='SET NULL'),
    )

    location_types_id = Column(
        Integer,
        ForeignKey('location_types.location_types_id', ondelete='SET NULL')
    )

    construction_companies_id = Column(
        Integer,
        ForeignKey('construction_companies.construction_companies_id', ondelete='CASCADE'),
        nullable=False
    )

    oksm_id = Column(
        Integer,
        ForeignKey('OKSM.oksm_id', ondelete='SET NULL'),
    )

    coordinates_id = Column(
        Integer,
        ForeignKey('coordinates.coordinates_id')
    )

    id_fias = Column(
        Integer,
        ForeignKey('fias.id')
    )

    organizations_id = Column(
        UUID,
        ForeignKey('{schema}.organizations.organizations_id'.format(schema=ORGANIZATION_SCHEMA)),
        nullable=True
    )

    # --------- relationships --------- #

    construction_category = relationship(
        'ConstructionCategory',
        back_populates='construction'
    )

    subcategories_list = relationship(
        'SubcategoryList',
        back_populates='construction'
    )

    commission = relationship(
        'Commission',
        back_populates='construction'
    )

    military_unit = relationship(
        'MilitaryUnit',
        foreign_keys=[idMU]
    )

    military_district = relationship(
        'MilitaryUnit',
        foreign_keys=[military_district_id]
    )

    construction_objects = relationship(
        'ConstructionObject',
        back_populates='construction',
        order_by='desc(ConstructionObject.planned_date)',
        lazy='joined',
        passive_deletes=True,
    )

    coordinate = relationship(
        'Coordinate',
        back_populates='construction'
    )

    location_type = relationship(
        'LocationType'
    )

    construction_company = relationship(
        'ConstructionCompany'
    )

    construction_type = relationship(
        'ConstructionType',
        back_populates='constructions'
    )

    contracts = relationship(
        'Contract',
        back_populates='construction',
        passive_deletes=True
    )

    organization = relationship(
        'Organization'
    )

    dynamic_raw = relationship(
        'ConstructionDynamic',
        order_by='desc(ConstructionDynamic.reporting_date)',
        lazy='dynamic'
    )

    oksm = relationship('OKSM')
    fias = relationship('FIAS')

    # --------- calculated_fields --------- #

    @hybrid_property
    def actually_entered(self):
        return sum(filter(lambda x: x.fact_date, self.construction_objects))

    @hybrid_property
    def readiness(self):
        return sum(construction_object.readiness for construction_object in self.construction_objects)

    @hybrid_property
    def planned_date(self):
        return self.construction_objects[0].planned_date if self.construction_objects else None

    @hybrid_property
    def dynamic(self):
        return self.dynamic_raw.filter_by(from_sakura=True).first()
