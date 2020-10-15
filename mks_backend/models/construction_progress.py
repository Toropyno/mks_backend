from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date,
    DECIMAL,
    TIMESTAMP,
    UniqueConstraint,
    CheckConstraint,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from mks_backend.models import Base


class ConstructionProgress(Base):

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
        nullable=False,
        passive_deletes=True,
    )

    progress_statuses_id = Column(
        Integer,
        ForeignKey('progress_statuses.progress_statuses_id', ondelete='CASCADE'),
        nullable=False,
    )

    construction_object = relationship(
        'ConstructionObject',
        back_populates='construction_progress'
    )

    progress_status = relationship(
        'ProgressStatus',
        back_populates='construction_progress'
    )
