from sqlalchemy import Column, BigInteger, DateTime, REAL, Text

from data_models.common_db import Base


class DarkSkyTemplate(object):
    __table_args__ = {'schema': 'auxiliary_data'}

    uid = Column(BigInteger, primary_key=True, autoincrement=True)
    gid = Column(BigInteger, nullable=False)
    timestamp = Column(DateTime, nullable=False)
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


class LosAngeles5000mGridMeoDarkSky201801(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201801'


class LosAngeles5000mGridMeoDarkSky201802(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201802'


class LosAngeles5000mGridMeoDarkSky201803(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201803'


class LosAngeles5000mGridMeoDarkSky201804(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201804'


class LosAngeles5000mGridMeoDarkSky201805(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201805'


class LosAngeles5000mGridMeoDarkSky201806(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201806'


class LosAngeles5000mGridMeoDarkSky201807(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201807'


class LosAngeles5000mGridMeoDarkSky201808(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201808'


class LosAngeles5000mGridMeoDarkSky201809(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201809'


class LosAngeles5000mGridMeoDarkSky201810(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201810'


class LosAngeles5000mGridMeoDarkSky201811(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201811'


class LosAngeles5000mGridMeoDarkSky201812(DarkSkyTemplate, Base):
    __tablename__ = 'los_angeles_5000m_grid_meo_darksky_201812'


class SaltLakeCity5000mGridMeoDarkSky201703201803(DarkSkyTemplate, Base):
    __tablename__ = 'salt_lake_city_5000m_grid_meo_darksky_201703_201803'


# class Utah5000mGridMeoDarkSky2018(DarkSkyTemplate, Base):
#     __tablename__ = 'utah_5000m_grid_meo_darksky_2018'
#
#     uid_seq = Sequence('utah_5000m_grid_meo_darksky_2018_uid_seq')
#     uid = Column(BigInteger, primary_key=True, nullable=False, server_default=uid_seq.next_value())
#     gid = Column(BigInteger, nullable=False)
#     timestamp = Column(DateTime, nullable=False)
#
#
# class Utah5000mGridMeoDarkSky2017(DarkSkyTemplate, Base):
#     __tablename__ = 'utah_5000m_grid_meo_darksky_2017'
#
#     uid_seq = Sequence('utah_5000m_grid_meo_darksky_2017_uid_seq')
#     uid = Column(BigInteger, primary_key=True, nullable=False, server_default=uid_seq.next_value())
#     gid = Column(BigInteger, nullable=False)
#     timestamp = Column(DateTime, nullable=False)

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
    cloud_cover real,
    uv_index integer,
    visibility real,
    ozone real
);


"""