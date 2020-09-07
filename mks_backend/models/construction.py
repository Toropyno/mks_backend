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
    construction_categories_id = Column(Integer, ForeignKey('construction_categories.construction_categories_id'))
    subcategories_list_id = Column(Integer, ForeignKey('subcategories_list.subcategories_list_id'))
    is_critical = Column(Boolean, nullable=False)
    commission_id = Column(Integer, ForeignKey('commission.commission_id', ondelete='CASCADE'), nullable=False)
    idMU = Column(Integer, ForeignKey('military_unit.idMU'))
    contract_date = Column(DATE, nullable=False)
    object_amount = Column(Integer, CheckConstraint('object_amount>0'), nullable=False)
    planned_date = Column(DATE, nullable=False)

    construction_categories = relationship(
        'ConstructionCategories',
        back_populates='construction'
    )

    subcategories_list = relationship(
        'SubcategoriesList',
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
