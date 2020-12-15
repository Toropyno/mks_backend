from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class Zone(Base):
    __tablename__ = 'zones'

    zones_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    construction_object = relationship(
        'ConstructionObject',
        back_populates='zone'
    )

    object_categories = relationship(
        'ObjectCategory',
        secondary='object_categories_list',
        back_populates='zones'
    )
