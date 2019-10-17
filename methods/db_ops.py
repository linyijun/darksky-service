from data_models.common_db import session, engine


def create_darksky_table(darksky_obj):

    try:
        darksky_obj.__table__.drop(bind=engine, checkfirst=True)
        darksky_obj.__table__.create(bind=engine)

    except Exception as e:
        print(e)
        exit(1)


def request_target_locations(location_obj):

    results = session.query(location_obj).with_entities(*[location_obj.gid, location_obj.lon, location_obj.lat]).all()

    loc_dict = {}

    if not results:
        return {'status': -1, 'msg': 'No target locations.', 'data': loc_dict}
    else:
        for res in results:
            loc_dict[res.gid] = (res.lon, res.lat)
        return {'status': 1, 'msg': '', 'data': loc_dict}


def insert_new_data(data, darksky_obj):

    new_data = []

    for item in data:
        obj = darksky_obj(gid=item['gid'],
                          timestamp=item['timestamp'],
                          summary=item.get('summary'),
                          icon=item.get('icon'),
                          precip_intensity=item.get('precipIntensity'),
                          precip_probability=item.get('precipProbability'),
                          temperature=item.get('temperature'),
                          apparent_temperature=item.get('apparentTemperature'),
                          dew_point=item.get('dewPoint'),
                          humidity=item.get('humidity'),
                          pressure=item.get('pressure'),
                          wind_speed=item.get('windSpeed'),
                          wind_bearing=item.get('windBearing'),
                          cloud_cover=item.get('cloudCover'),
                          uv_index=item.get('uvIndex'),
                          visibility=item.get('visibility'),
                          ozone=item.get('ozone'))
        new_data.append(obj)

    session.add_all(new_data)
    session.commit()
