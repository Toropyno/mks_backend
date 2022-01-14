from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.orm import relationship

from mks_backend.session import Base


class ConstructionCategory(Base):
    __tablename__ = 'construction_categories'

    construction_categories_id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)

    subcategories = relationship(
        'ConstructionSubcategory',
        secondary='subcategories_list'
    )
