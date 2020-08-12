from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    VARCHAR,
    Boolean,
    DATE,
    CheckConstraint,
)

from mks_backend.models import Base


class Construction(Base):

    __tablename__ = 'construction'
    construction_id = Column(Integer, primary_key=True)
    project_code = Column(VARCHAR(40), nullable=False)
    project_name = Column(VARCHAR(255), nullable=False)
    construction_categories_id = Column(Integer, ForeignKey('construction_categories.id'))
    subcategories_list_id = Column(Integer, ForeignKey('subcategories_list.id'))
    commission_id = Column(Integer, ForeignKey('commission_id.id'))
    idMU = Column(Integer, ForeignKey('military_unit.id'))
    is_critical = Column(Boolean, nullable=False)
    contract_date = Column(DATE, nullable=False)
    object_amount = Column(Integer, CheckConstraint('object_amount>0'), nullable=False)
    planned_date = Column(DATE, nullable=False)
