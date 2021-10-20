from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    VARCHAR,
    DATE
)
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class WorkTrip(Base):
    """
    Реестр поездок руководства МО РФ
    """
    __tablename__ = 'work_trips'

    work_trips_id = Column(Integer, primary_key=True)
    trip_date = Column(DATE, nullable=False)
    trip_name = Column(VARCHAR(255), nullable=False)
    escort_officer = Column(VARCHAR(100), nullable=False)

    leadership_positions_id = Column(
        Integer,
        ForeignKey('leadership_positions.leadership_positions_id'),
        nullable=False
    )

    protocol_id = Column(
        Integer,
        ForeignKey('protocol.protocol_id', ondelete='SET NULL'),
        nullable=True
    )

    # --------- relationships --------- #

    leadership_position = relationship(
        'LeadershipPosition'
    )

    protocol = relationship(
        'Protocol',
    )

    constructions = relationship(
        'Construction',
        secondary='visited_objects'
    )

    work_trip_files = relationship(
        'WorkTripFiles',
        cascade='all, delete-orphan'
    )
