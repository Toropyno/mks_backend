from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    DATE,
    TIMESTAMP,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class ConstructionDocument(Base):

    __tablename__ = 'construction_documents'

    construction_documents_id = Column(Integer, primary_key=True)
    doc_number = Column(VARCHAR(40), nullable=False)
    doc_date = Column(DATE, nullable=False)
    doc_name = Column(VARCHAR(255))
    note = Column(VARCHAR(1000))
    upload_date = Column(TIMESTAMP)

    construction_id = Column(
        Integer,
        ForeignKey('construction.construction_id', ondelete='CASCADE'),
        nullable=False,
    )

    doctypes_id = Column(
        Integer,
        ForeignKey('doctypes.doctypes_id', ondelete='CASCADE'),
        nullable=False,
    )

    idfilestorage = Column(
        UUID,
        ForeignKey('filestorage.idfilestorage', ondelete='SET NULL'),
    )

    # --------- relationships --------- #

    parent = relationship(
        'ConstructionObject',
        secondary='object_documents',
        back_populates='documents'
    )

    doc_type = relationship(
        'DocType',
        back_populates='documents'
    )

    file_storage = relationship(
        'Filestorage',
        single_parent=True,
        cascade='all, delete-orphan'
    )
