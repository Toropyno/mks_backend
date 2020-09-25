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

from mks_backend.models import Base


class Construction(Base):

    __tablename__ = 'construction'
    construction_id = Column(Integer, primary_key=True, autoincrement=True)
    project_code = Column(VARCHAR(40), unique=True, nullable=False)
    project_name = Column(VARCHAR(255), nullable=False)
    construction_categories_id = Column(Integer, ForeignKey('construction_categories.construction_categories_id',
                                                            ondelete='SET NULL'))
    subcategories_list_id = Column(Integer, ForeignKey('subcategories_list.subcategories_list_id',
                                                       ondelete='SET NULL'))
    is_critical = Column(Boolean, nullable=False)
    commission_id = Column(Integer, ForeignKey('commission.commission_id', ondelete='SET NULL'), nullable=False)
    idMU = Column(Integer, ForeignKey('military_unit.idMU'))
    contract_date = Column(DATE, nullable=False)
    object_amount = Column(
        Integer,
        CheckConstraint('object_amount>0'),
        nullable=False
    )
    planned_date = Column(DATE, nullable=False)
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
    id_fias = Column(Integer)  # ForeignKey()
    address = Column(VARCHAR(1000))
    note = Column(VARCHAR(1000))
    coordinates_id = Column(Integer, ForeignKey('coordinates.coordinates_id'))

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
