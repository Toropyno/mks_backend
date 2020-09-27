from uuid import UUID

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    TIMESTAMP,
    VARCHAR,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from mks_backend.models import Base


class ObjectFile(Base):

    __tablename__ = 'object_files'
    object_files_id = Column(Integer, primary_key=True, autoincrement=True)
    idfilestorage = Column(
        UUID,
        ForeignKey('filestorage.idfilestorage', ondelete='CASCADE'),
        nullable=False,
    )

    construction_objects_id = Column(
        Integer,
        ForeignKey('construction_objects.construction_objects_id', ondelete='CASCADE'),
        nullable=False,
    )

    upload_date = Column(TIMESTAMP, default=func.now(), nullable=False)
    note = Column(VARCHAR(1000))

    construction_object = relationship(
        'ConstructionObject',
        back_populates='object_files'
    )

    file_storage = relationship(
        'Filestorage',
        back_populates='object_files'
    )

