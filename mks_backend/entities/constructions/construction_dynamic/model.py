from sqlalchemy import (DATE, TIMESTAMP, VARCHAR, Boolean, CheckConstraint, Column, ForeignKey, Integer,
                        UniqueConstraint, func)

from mks_backend.session import Base


class ConstructionDynamic(Base):
    """
    Ход строительсвта ИСП
    """

    __tablename__ = 'construction_dynamics'
    __table_args__ = (
        UniqueConstraint(
            'reporting_date',
            'construction_id',
            'from_sakura',
            name='construction_dynamics_ak'
        ),
    )

    construction_dynamics_id = Column(Integer, primary_key=True)
    reporting_date = Column(DATE, nullable=False)
    from_sakura = Column(Boolean, default=False, nullable=False)
    update_datetime = Column(TIMESTAMP, default=func.now(), nullable=False)

    people_plan = Column(Integer, CheckConstraint('people_plan>=0'), nullable=False)
    people = Column(Integer, CheckConstraint('people>=0'), nullable=False)
    equipment_plan = Column(Integer, CheckConstraint('equipment_plan>=0'), nullable=False)
    equipment = Column(Integer, CheckConstraint('equipment>=0'), nullable=False)

    description = Column(VARCHAR(255))
    reason = Column(VARCHAR(100))
    problems = Column(VARCHAR(1000))

    construction_id = Column(ForeignKey('construction.construction_id', ondelete='CASCADE'), nullable=False)
