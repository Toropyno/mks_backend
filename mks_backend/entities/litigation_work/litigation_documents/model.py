from sqlalchemy import DATE, TIMESTAMP, VARCHAR, Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mks_backend.db_schemas import COURTS_SCHEMA
from mks_backend.session import Base


class LitigationDocument(Base):
    __tablename__ = 'litigation_documents'
    __table_args__ = (
        UniqueConstraint(
            'litigation_id',
            'doctypes_id',
            'doc_number',
            'doc_date',
            name='litigation_document_unique'
        ),
        {'schema': COURTS_SCHEMA}
    )

    litigation_documents_id = Column(Integer, primary_key=True)
    doc_number = Column(VARCHAR(40), nullable=False)
    doc_date = Column(DATE, nullable=False)
    doc_name = Column(VARCHAR(255))
    note = Column(VARCHAR(1000))
    upload_date = Column(TIMESTAMP)

    litigation_id = Column(
        Integer,
        ForeignKey('{}.litigation.litigation_id'.format(COURTS_SCHEMA), ondelete='CASCADE'),
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

    doc_type = relationship('DocType')

    file_storage = relationship(
        'Filestorage',
        single_parent=True,
        cascade='all, delete-orphan'
    )
