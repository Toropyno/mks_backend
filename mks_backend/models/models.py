from uuid import uuid4
from datetime import date

from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, Date, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from .meta import Base


class Protocol(Base):
    __tablename__ = 'protocol'
    protocol_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    protocol_num = Column(VARCHAR(20), nullable=False)
    protocol_date = Column(Date, nullable=False, default=func.current_date())
    meetings_type_id = Column(Integer, ForeignKey('meeting.meetings_type_id'))
    protocol_name = Column(VARCHAR(255), nullable=False)
    note = Column(VARCHAR(2000))
    idfilestorage = Column(UUID, ForeignKey('filestorage.idfilestorage', ondelete='CASCADE'))

    def __json__(self, request):
        json_exclude = getattr(self, '__json_exclude__', set())

        json_protocol = dict()
        for key, value in self.__dict__.items():
            if key.startswith('_') or key in json_exclude:
                continue
            elif isinstance(value, date):
                value = str(value)

            json_protocol[key] = value

        return json_protocol

    def __str__(self):
        return f'id={self.protocol_id}, protocol_number={self.protocol_num}'


class Filestorage(Base):
    __tablename__ = 'filestorage'
    idfilestorage = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    filename = Column(VARCHAR(255), nullable=False)
    uri = Column(VARCHAR(1024), nullable=False)
    filesize = Column(Integer, default=0)
    mimeType = Column(VARCHAR(30))
    createdOn = Column(TIMESTAMP(timezone=True), default=func.now())
    description = Column(VARCHAR(100))
    authorid = Column(Integer)


class Meeting(Base):
    __tablename__ = 'meeting'
    meetings_type_id = Column(Integer, primary_key=True, nullable=False)
