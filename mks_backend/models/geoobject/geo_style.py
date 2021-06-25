from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from mks_backend.session import Base


class GeoStyle(Base):
    __tablename__ = 'geo_styles'
    geo_style_id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(String, nullable=False)
    library_id = Column(UUID, default=uuid4, nullable=False)
    classif_id = Column(String, nullable=False)
