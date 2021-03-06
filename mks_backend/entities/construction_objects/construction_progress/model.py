from sqlalchemy import DECIMAL, TIMESTAMP, CheckConstraint, Column, Date, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.session import Base


class ConstructionProgress(Base):
    """
    Ход строительства (здания и сооружения)
    """
    __tablename__ = 'construction_progress'

    __table_args__ = (
        UniqueConstraint(
            'construction_progress_id',
            'reporting_date',
            name='construction_progress_unique'
        ),
    )

    construction_progress_id = Column(Integer, primary_key=True, autoincrement=True)
    reporting_date = Column(Date, nullable=False)
    update_datetime = Column(TIMESTAMP, default=func.now())

    people_plan = Column(Integer, CheckConstraint('people_plan>=0'), nullable=False)
    equipment_plan = Column(Integer, CheckConstraint('equipment_plan>=0'), nullable=False)

    readiness = Column(
        DECIMAL(17, 2),
        CheckConstraint('(readiness>=0) AND (readiness<=100)'),
        nullable=False
    )

    people = Column(
        Integer,
        CheckConstraint('people>=0'),
        nullable=False
    )

    equipment = Column(
        Integer,
        CheckConstraint('equipment>=0'),
        nullable=False
    )

    construction_objects_id = Column(
        Integer,
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'),
        nullable=False
    )

    progress_statuses_id = Column(
        Integer,
        ForeignKey('progress_statuses.progress_statuses_id', ondelete='CASCADE'),
        nullable=False,
    )

    # --------- relationships --------- #

    construction_object = relationship(
        'ConstructionObject',
        back_populates='construction_progress'
    )

    progress_status = relationship(
        'ProgressStatus',
        back_populates='construction_progress'
    )
