from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from mks_backend.session import Base


class GeoObject(Base):
    __tablename__ = 'geo_objects'

    geo_object_id = Column(Integer, primary_key=True, autoincrement=True)
    coordinate_id = Column(Integer, ForeignKey('coordinates.coordinates_id'))
    style_id = Column(Integer, ForeignKey('geo_styles.geo_style_id'), nullable=False, default=1)
    projection = Column(String, nullable=False, default='EPSG:4326')

    coordinate = relationship('Coordinate')
    geo_object__cross__user = relationship('GeoObjectCrossUser')
    style = relationship('GeoStyle')
