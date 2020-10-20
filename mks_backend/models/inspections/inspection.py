from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    DATE,
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class Inspection(Base):
    """
    Проверки объектов строительства
    """
    __tablename__ = 'inspections'

    __table_args__ = (
        UniqueConstraint(
            'insp_date',
            'insp_name',
            name='inspection_unique'
        ),
    )
    inspections_id = Column(Integer, primary_key=True)
    insp_date = Column(DATE, nullable=False)
    insp_name = Column(VARCHAR(255), nullable=False)
    inspector = Column(VARCHAR(100), nullable=False)
    insp_result = Column(VARCHAR(2000), nullable=True)

    def __str__(self):
        return 'Проверка id={id}, name={name}'.format(
            id=self.inspections_id,
            name=self.insp_name,
        )
