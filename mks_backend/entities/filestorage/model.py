from uuid import uuid4

from sqlalchemy import TIMESTAMP, VARCHAR, Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func

from mks_backend.session import Base


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

    @hybrid_property
    def size(self):
        filesize = self.filesize / 1024  # to Kbytes

        if filesize >= 1024:
            filesize = filesize / 1024
            filesize = '{:.1f}Мб'.format(filesize)
        else:
            filesize = '{:.1f}Кб'.format(filesize)

        return filesize
