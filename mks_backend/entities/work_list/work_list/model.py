from sqlalchemy import DATE, DECIMAL, VARCHAR, CheckConstraint, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class WorkList(Base):
    """
    Перечень проводимых работ
    """

    __tablename__ = 'works_list'

    __table_args__ = (
        UniqueConstraint(
            'construction_objects_id',
            'element_types_id',
            name='worklist_unique'
        ),
    )

    works_list_id = Column(Integer, primary_key=True)

    element_description = Column(VARCHAR(500), nullable=True)
    begin_date = Column(DATE, nullable=False)
    work_description = Column(VARCHAR(500), nullable=True)
    relevance_date = Column(DATE, nullable=False)
    note = Column(VARCHAR(1000), nullable=True)

    element_types_id = Column(
        Integer,
        ForeignKey('element_types.element_types_id', ondelete='CASCADE'),
        nullable=False
    )

    weight = Column(
        Integer,
        CheckConstraint('weight>0 AND weight<=100'),
        nullable=False
    )

    end_date = Column(
        DATE,
        CheckConstraint('end_date>=begin_date'),
        nullable=False
    )

    plan = Column(
        DECIMAL(17, 1),
        CheckConstraint('plan>0'),
        nullable=False
    )

    fact = Column(
        DECIMAL(17, 1),
        CheckConstraint('fact>=0 AND fact<=plan'),
        nullable=False
    )

    unit_id = Column(
        Integer,
        ForeignKey('measure_units.unit_id'),
        nullable=False
    )

    work_types_id = Column(
        Integer,
        ForeignKey('work_types.work_types_id', ondelete='SET NULL'),
        nullable=True
    )

    construction_objects_id = Column(
        Integer,
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'),
        nullable=False
    )

    # --------- relationships --------- #

    measure_unit = relationship(
        'MeasureUnit'
    )

    work_type = relationship(
        'WorkType'
    )

    construction_object = relationship(
        'ConstructionObject',
        back_populates='worklist'
    )

    element_type = relationship(
        'ElementType',
        back_populates='works_list'
    )
