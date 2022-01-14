from sqlalchemy import TIMESTAMP, VARCHAR, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.session import Base


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

    # --------- relationships --------- #

    file_storage = relationship(
        'Filestorage',
        single_parent=True,
        cascade='all, delete-orphan'
    )
