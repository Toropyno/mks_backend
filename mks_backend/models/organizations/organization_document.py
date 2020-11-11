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

from mks_backend.models import Base, ORGANIZATION_SCHEMA


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
        {'schema': ORGANIZATION_SCHEMA},
    )

    organization_documents_id = Column(Integer, primary_key=True)
    doc_name = Column(VARCHAR(255))
    note = Column(VARCHAR(1000))
    upload_date = Column(TIMESTAMP, default=func.now())

    doc_date = Column(DATE, nullable=False)
    doc_number = Column(VARCHAR(40))

    organizations_id = Column(
        UUID,
        ForeignKey('{schema}.organizations.organizations_id'.format(schema=ORGANIZATION_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    doctypes_id = Column(
        Integer,
        ForeignKey('doctypes.doctypes_id', ondelete='CASCADE'),
        nullable=False
    )

    idfilestorage = Column(
        UUID,
        ForeignKey('filestorage.idfilestorage', ondelete='SET NULL')
    )

    # --------- relationships --------- #

    file_storage = relationship(
        'Filestorage'
    )

    doc_type = relationship(
        'DocType'
    )

    organization = relationship(
        'Organization',
        back_populates='organization_documents'
    )
