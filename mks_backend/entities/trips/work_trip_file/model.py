from sqlalchemy import TIMESTAMP, VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class WorkTripFile(Base):
    __tablename__ = 'work_trip_files'

    idfilestorage = Column(
        UUID,
        ForeignKey('filestorage.idfilestorage', ondelete='CASCADE'),
        primary_key=True,
    )
    work_trips_id = Column(
        Integer,
        ForeignKey('work_trips.work_trips_id', ondelete='CASCADE')
    )
    note = Column(VARCHAR(1000))
    upload_date = Column(TIMESTAMP)

    file_storage = relationship(
        'Filestorage',
        single_parent=True,
        cascade='all, delete-orphan'
    )
