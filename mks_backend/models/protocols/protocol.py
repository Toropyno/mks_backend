from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    VARCHAR,
    Date,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.models import Base


class Protocol(Base):

    __tablename__ = 'protocol'

    protocol_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    protocol_num = Column(VARCHAR(20), nullable=False)
    protocol_date = Column(Date, nullable=False, default=func.current_date())
    protocol_name = Column(VARCHAR(255), nullable=False)
    note = Column(VARCHAR(2000))

    meetings_type_id = Column(
        Integer,
        ForeignKey('meeting.meetings_type_id')
    )

    idfilestorage = Column(
        UUID,
        ForeignKey('filestorage.idfilestorage', ondelete='CASCADE')
    )

    # --------- relationships --------- #

    meeting = relationship(
        'Meeting',
        back_populates='protocols'
    )

    filestorage = relationship(
        'Filestorage',
        back_populates='protocols'
    )

    def __str__(self):
        return 'id={id}, protocol_number={number}'.format(
            id=self.protocol_id,
            number=self.protocol_num
        )
