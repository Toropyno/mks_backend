from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class ConstructionSubcategory(Base):

    __tablename__ = 'construction_subcategories'
    construction_subcategories_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    parent = relationship(
        'ConstructionCategory',
        secondary='subcategories_list',
        back_populates='child'
    )
