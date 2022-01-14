from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint

from mks_backend.session import Base


class VisitedObject(Base):
    """
    Перечень посещенных объектов
    """
    __tablename__ = 'visited_objects'

    __table_args__ = (
        PrimaryKeyConstraint(
            'work_trips_id',
            'construction_id',
            name='visited_objects_pk'
        ),
    )

    work_trips_id = Column(
        Integer,
        ForeignKey('work_trips.work_trips_id', ondelete='CASCADE'),
        nullable=False
    )

    construction_id = Column(
        Integer,
        ForeignKey('construction.construction_id', ondelete='CASCADE'),
        nullable=False
    )
