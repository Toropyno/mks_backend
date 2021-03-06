from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class Zone(Base):
    __tablename__ = 'zones'

    zones_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    object_categories = relationship(
        'ObjectCategory',
        secondary='object_categories_list'
    )
