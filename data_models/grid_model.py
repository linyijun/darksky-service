from sqlalchemy import Column, Float, BigInteger
from geoalchemy2 import Geometry

from data_models.common_db import Base


class GridTemplate(object):
    __table_args__ = {'schema': 'geographic_data'}

    gid = Column(BigInteger, nullable=False, primary_key=True)
    centroid = Column(Geometry('POINT', srid=4326))
    lon = Column(Float(53))
    lat = Column(Float(53))
    geom = Column(Geometry('POLYGON', srid=4326))


class LosAngeles5000mGrid(GridTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid'


class SalkLakeCity5000mGrid(GridTemplate, Base):
    __tablename__ = 'salt_lake_city_5000m_grid'
