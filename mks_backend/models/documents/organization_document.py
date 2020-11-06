from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    DATE,
    TIMESTAMP,
    ForeignKey,
    UniqueConstraint,
)

from mks_backend.models import Base


class OrganizationDocument(Base):

    __tablename__ = 'organization_documents'

    __table_args__ = (
        UniqueConstraint(
            'organizations_id',
            'doctypes_id',
            'doc_date',
            'doc_number',
            name='organization_documents_unique'
        ),
    )

    organization_documents_id = Column(Integer, primary_key=True)
    doc_name = Column(VARCHAR(255))
    note = Column(VARCHAR(1000))
    upload_date = Column(TIMESTAMP, default=func.now())

    doc_date = Column(DATE, unique=True, nullable=False)
    doc_number = Column(VARCHAR(40), unique=True)

    organizations_id = Column(
        UUID,
        ForeignKey('organizations.organizations_id', ondelete='CASCADE'),
        unique=True,
        nullable=False
    )

    doctypes_id = Column(
        Integer,
        ForeignKey('doctypes.doctypes_id', ondelete='CASCADE'),
        unique=True,
        nullable=False
    )

    idfilestorage = Column(
        UUID,
        ForeignKey('filestorage.idfilestorage', ondelete='SET NULL')
    )

    # --------- relationships --------- #

    filestorage = relationship(
        'Filestorage',
        back_populates='organization_documents'
    )

    organization = relationship(
        'Organization',
        back_populates='organization_document'
    )

    doc_type = relationship(
        'DocType',
        back_populates='organization_document'
    )
