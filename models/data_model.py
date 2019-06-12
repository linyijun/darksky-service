from sqlalchemy import Column, BigInteger, DateTime, REAL, Text, Sequence

from utils.common_db import Base


class DarkSkyTemplate(object):
    __table_args__ = {'schema': 'auxiliary_data'}

    summary = Column(Text)
    icon = Column(Text)
    precip_intensity = Column(REAL)
    precip_probability = Column(REAL)
    temperature = Column(REAL)
    apparent_temperature = Column(REAL)
    dew_point = Column(REAL)
    humidity = Column(REAL)
    pressure = Column(REAL)
    wind_speed = Column(REAL)
    wind_bearing = Column(REAL)
    cloud_cover = Column(REAL)
    uv_index = Column(REAL)
    visibility = Column(REAL)
    ozone = Column(REAL)


class LosAngeles5000mGridMeoDarkSky2018(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_2018'

    uid_seq = Sequence('los_angeles_5000m_grid_meo_darksky_2018_uid_seq')
    uid = Column(BigInteger, primary_key=True, nullable=False, server_default=uid_seq.next_value())
    gid = Column(BigInteger, nullable=False)
    timestamp = Column(DateTime, nullable=False)


"""
Create Darksky Table template

DROP TABLE IF EXISTS auxiliary_data.los_angeles_5000m_grid_meo_darksky_2018;
CREATE TABLE auxiliary_data.los_angeles_5000m_grid_meo_darksky_2018 (
    uid BIGSERIAL PRIMARY KEY,
    gid integer NOT NULL,
    timestamp timestamp with time zone NOT NULL,
    summary text,
    icon text,
    precip_intensity real,
    precip_probability real,
    temperature real,
    apparent_temperature real,
    dew_point real,
    humidity real,
    pressure real,
    wind_speed real,
    wind_bearing real,
    uv_index integer,
    visibility real,
    ozone real,
);


"""