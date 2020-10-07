from uuid import uuid4

from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    TIMESTAMP,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.models import Base


class Filestorage(Base):

    __tablename__ = 'filestorage'
    idfilestorage = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    filename = Column(VARCHAR(255), nullable=False)
    uri = Column(VARCHAR(1024), nullable=False)
    filesize = Column(Integer, default=0)
    mimeType = Column(VARCHAR(45))
    createdOn = Column(TIMESTAMP(timezone=True), default=func.now())
    description = Column(VARCHAR(100))
    authorid = Column(Integer)

    protocols = relationship(
        'Protocol',
        back_populates='filestorage',
        passive_deletes=True
    )

    document = relationship(
        'ConstructionDocument',
        back_populates='file_storage'
    )

    object_files = relationship(
        'ObjectFile',
        back_populates='file_storage'
    )
