from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from mks_backend.models import Base


class ConstructionCategory(Base):

    __tablename__ = 'construction_categories'
    construction_categories_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    construction = relationship(
        'Construction',
        back_populates='construction_categories'
    )

    child = relationship(
        'ConstructionSubcategory',
        secondary='subcategories_list',
        back_populates='parent'
    )
