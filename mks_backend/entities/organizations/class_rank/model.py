from sqlalchemy import Column, INTEGER, VARCHAR

from mks_backend.session import Base
from mks_backend.db_schemas import ORGANIZATION_SCHEMA


class ClassRank(Base):
    """
    Словарь 'Классные чины'
    """

    __tablename__ = 'class_ranks'

    __table_args__ = {'schema': ORGANIZATION_SCHEMA}

    class_ranks_id = Column(INTEGER, primary_key=True, comment='Ид классного чина')
    fullname = Column(VARCHAR(255), unique=True, nullable=False, comment='Наименование')
