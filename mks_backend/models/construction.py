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
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from mks_backend.models import Base


class Construction(Base):

    __tablename__ = 'construction'
    construction_id = Column(Integer, primary_key=True, autoincrement=True)
    project_code = Column(VARCHAR(40), unique=True, nullable=False)
    project_name = Column(VARCHAR(255), nullable=False)
    contract_date = Column(DATE, nullable=False)
    is_critical = Column(Boolean, nullable=False)
    planned_date = Column(DATE, nullable=False)
    id_fias = Column(Integer)  # ForeignKey()
    address = Column(VARCHAR(1000))
    note = Column(VARCHAR(1000))

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
        ForeignKey('commission.commission_id', ondelete='SET NULL'),
        nullable=False
    )

    idMU = Column(
        Integer,
        ForeignKey('military_unit.idMU')
    )

    object_amount = Column(
        Integer,
        CheckConstraint('object_amount>0'),
        nullable=False
    )

    construction_types_id = Column(
        Integer,
        ForeignKey('construction_types.construction_types_id'),
        nullable=False
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
        ForeignKey('OKSM.oksm_id'),
        nullable=False
    )

    coordinates_id = Column(
        Integer,
        ForeignKey('coordinates.coordinates_id')
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
        back_populates='construction'
    )

    construction_objects = relationship(
        'ConstructionObject',
        back_populates='construction',
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

    oksm = relationship(
        'OKSM'
    )

    type = relationship(
        'ConstructionType'
    )

    # --------- calculated_fields --------- #

    @hybrid_property
    def calculated_fields(self):
        plan = 0
        actually = 0
        entered_additionally = 0
        readiness = 0
        workers = 0
        equipment = 0
        now_year = datetime.now().year

        for construction_object in self.construction_objects:
            if construction_object.planned_date.year == now_year:
                plan += 1
            if construction_object.planned_date.year == construction_object.fact_date.year == now_year:
                actually += 1
            if construction_object.fact_date.year == now_year != construction_object.planned_date.year:
                entered_additionally += 1

            readiness += construction_object.readiness
            workers += construction_object.workers
            equipment += construction_object.equipment
        difference = plan - actually

        return {
            'plan': plan,
            'actually': actually,
            'difference': difference,
            'enteredAdditionally': entered_additionally,
            'readiness': format(readiness, '.3f'),
            'workers': workers,
            'equipment': equipment,
        }
