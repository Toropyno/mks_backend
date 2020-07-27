from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Date, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from .meta import Base


class Protocol(Base):
    __tablename__ = 'protocol'
    protocol_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    protocol_num = Column(VARCHAR(20), nullable=False)
    protocol_date = Column(Date, nullable=False)
    meetings_type_id = Column(Integer, ForeignKey('meeting.meetings_type_id'))
    protocol_name = Column(VARCHAR(255), nullable=False)
    note = Column(VARCHAR(2000))
    idfilestorage = Column(UUID, ForeignKey('filestorage.idfilestorage'))


class Filestorage(Base):
    __tablename__ = 'filestorage'
    idfilestorage = Column(UUID, primary_key=True, nullable=False)
    filename = Column(VARCHAR(255), nullable=False)
    uri = Column(VARCHAR(1024), nullable=False)
    filesize = Column(Integer, default=0)
    mimeType = Column(VARCHAR(30))
    createdOn = Column(TIMESTAMP(timezone=True))
    description = Column(VARCHAR(100))
    authorid = Column(Integer)


class Meeting(Base):
    __tablename__ = 'meeting'
    meetings_type_id = Column(Integer, primary_key=True, nullable=False)
