from sqlalchemy import VARCHAR, Column, Date, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mks_backend.session import Base


class Protocol(Base):
    __tablename__ = 'protocol'
    __table_args__ = (
        UniqueConstraint(
            'protocol_num',
            'protocol_date',
            name='protocol_ak'
        ),
    )

    protocol_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    protocol_num = Column(VARCHAR(20), nullable=False)
    protocol_date = Column(Date, nullable=False, default=func.current_date())
    protocol_name = Column(VARCHAR(255), nullable=False)
    note = Column(VARCHAR(2000))
    signatory = Column(VARCHAR(255))

    meetings_type_id = Column(
        Integer,
        ForeignKey('meeting.meetings_type_id')
    )

    idfilestorage = Column(
        UUID,
        ForeignKey('filestorage.idfilestorage', ondelete='SET NULL')
    )

    # --------- relationships --------- #

    meeting = relationship(
        'Meeting',
    )

    filestorage = relationship(
        'Filestorage',
        single_parent=True,
        cascade='all, delete-orphan'
    )
