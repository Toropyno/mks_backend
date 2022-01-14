from sqlalchemy import TIMESTAMP, VARCHAR, Column, ForeignKey, Integer, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mks_backend.entities.filestorage import Filestorage
from mks_backend.entities.inspections.inspection import Inspection
from mks_backend.session import Base


class InspectionFile(Base):
    __tablename__ = 'inspection_files'

    upload_date = Column(TIMESTAMP, default=func.now(), nullable=False)
    note = Column(VARCHAR(1000), nullable=True)

    idfilestorage = Column(
        UUID,
        ForeignKey(Filestorage.idfilestorage, ondelete='CASCADE'),
        primary_key=True
    )

    inspections_id = Column(
        Integer,
        ForeignKey(Inspection.inspections_id, ondelete='CASCADE'),
        nullable=False
    )

    # --------- relationships --------- #

    file_storage = relationship(
        'Filestorage',
        single_parent=True,
        cascade='all, delete-orphan'
    )

    inspection = relationship(
        'Inspection',
        back_populates='files'
    )
