from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    TIMESTAMP,
    VARCHAR,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.models import Base


class ObjectFile(Base):

    __tablename__ = 'object_files'

    __table_args__ = (
        UniqueConstraint(
            'idfilestorage',
            'construction_objects_id',
            name='object_files_unique'
        ),
    )

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

    file_storage = relationship(
        'Filestorage',
        back_populates='object_files'
    )

    construction_object = relationship(
        'ConstructionObject',
        back_populates='object_files'
    )
