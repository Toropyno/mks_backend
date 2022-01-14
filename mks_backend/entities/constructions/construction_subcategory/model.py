from sqlalchemy import VARCHAR, Column, Integer

from mks_backend.session import Base


class ConstructionSubcategory(Base):
    __tablename__ = 'construction_subcategories'

    construction_subcategories_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fullname = Column(VARCHAR(255), unique=True, nullable=False)
