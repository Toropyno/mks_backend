from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint

from mks_backend.db_schemas import COURTS_SCHEMA
from mks_backend.session import Base


class LitigationSubject(Base):
    """
   Предметы судебных споров
    """
    __tablename__ = 'litigation_subject'

    __table_args__ = (
        PrimaryKeyConstraint(
            'litigation_id',
            'construction_id',
            name='litigation_subject_pk'
        ),
        {'schema': COURTS_SCHEMA},
    )

    litigation_id = Column(
        Integer,
        ForeignKey('{}.litigation.litigation_id'.format(COURTS_SCHEMA), ondelete='CASCADE'),
        nullable=False
    )

    construction_id = Column(
        Integer,
        ForeignKey('construction.construction_id', ondelete='CASCADE'),
        nullable=False
    )
