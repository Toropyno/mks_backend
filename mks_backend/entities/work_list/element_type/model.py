from sqlalchemy import (
    Column,
    Integer,
    VARCHAR
)
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class ElementType(Base):
    __tablename__ = 'element_types'

    element_types_id = Column(Integer, primary_key=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    works_list = relationship(
        'WorkList',
        back_populates='element_type'
    )
