from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date,
    DECIMAL, TIMESTAMP,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.models import Base


class ConstructionProgress(Base):
    __tablename__ = 'construction_progress'
    construction_progress_id = Column(Integer, primary_key=True, autoincrement=True)
    construction_objects_id = Column(
        Integer,
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'),
        nullable=False,
    )
    reporting_date = Column(Date, nullable=False)
    readiness = Column(DECIMAL(17, 2), nullable=False)
    people = Column(Integer, nullable=False)
    equipment = Column(Integer, nullable=False)
    progress_statuses_id = Column(Integer, nullable=False)
    update_datetime = Column(TIMESTAMP, nullable=False)
