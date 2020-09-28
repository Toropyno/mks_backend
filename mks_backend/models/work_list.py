from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    DATE,
    ForeignKey,
    CheckConstraint,
    DECIMAL
)
from mks_backend.models import Base


class WorkList(Base):
    """
    Перечень проводимых работ
    """
    __tablename__ = 'works_list'
    works_list_id = Column(Integer, primary_key=True)
    construction_objects_id = Column(
        Integer,
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'),
        nullable=False
    )
    element_types_id = Column(Integer)  # backlog MKSBRYANS-177
    element_description = Column(VARCHAR(500), nullable=True)
    weight = Column(Integer, CheckConstraint('weight>0 AND weight<=100'), nullable=False)
    begin_date = Column(DATE, nullable=False)
    end_date = Column(DATE, CheckConstraint('end_date>begin_date'), nullable=False)
    plan = Column(DECIMAL(17, 1), CheckConstraint('plan>0'), nullable=False)
    fact = Column(DECIMAL(17, 1), CheckConstraint('fact>=0 AND fact<=plan'), nullable=False)
    unit_id = Column(ForeignKey)
    work_types_id = Column()
    work_description = Column(VARCHAR(500), nullable=True)
    relevance_date = Column(DATE, nullable=False)
    note = Column(VARCHAR(1000), nullable=True)
