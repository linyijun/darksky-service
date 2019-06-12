import time

from methods.request_data import request_darksky_data
from models.common_db import session


def one_time_request(lon, lat, timestamp, config):

    option = {'lon': lon,
              'lat': lat,
              'timestamp': timestamp,
              'api_key': config['API_KEY']
              }

    bad_msg = ''
    for i in range(config['MAX_RETRY']):
        data = request_darksky_data(option)

        if data['status'] == 1:
            return data['data']
        else:
            bad_msg = data['msg']
            time.sleep(30)
            print('Retry requesting ({},{}) @{}: {}'.format(lon, lat, timestamp, i))
            continue

    print(bad_msg)
    return None


def multiple_times_request(time_list, loc_dict, config):

    for timestamp in time_list:
        dk_data = []

        for loc, coord in loc_dict.items():
            data = one_time_request(coord[0], coord[1], timestamp, config)
            if data:
                data['gid'], data['timestamp'] = loc, timestamp
                dk_data.append(data)
        insert_new_data(dk_data, config['DARKSKY_TABLE'])
        time.sleep(60)


def insert_new_data(data, darksky_obj):
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
        session.add(obj)
        session.commit()
