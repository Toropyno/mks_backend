from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    PrimaryKeyConstraint,
)

from mks_backend.models import Base


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

    def __str__(self):
        return 'Посещенный объект construction_id={c_id}, поездка work_trip_id={w_id}'.format(
            c_id=self.construction_id,
            w_id=self.work_trips_id
        )
