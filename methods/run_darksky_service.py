import time
import json
import requests

from methods.db_ops import *


def request_darksky_data(option):

    url = 'https://api.darksky.net/forecast/{api_key}/{lat},{lon},{timestamp}?' \
          'exclude=[minutely,hourly,daily,alerts,flags]' \
        .format(lat=option['lat'], lon=option['lon'], timestamp=option['timestamp'], api_key=option['api_key'])

    try:
        raw_data = requests.get(url)
        json_data = json.loads(raw_data.text)
        data = json_data.get('currently')
        return {'status': 1, 'msg': '', 'data': data}

    except Exception as e:
        return {'status': -1, 'msg': 'Request Darksky API Failed: {}'.format(e), 'data': {}}


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
            print('Retry requesting ({},{}) @{}: No. {} Time.'.format(lon, lat, timestamp, i))
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
        insert_new_data(dk_data, config['DARKSKY_OBJ'])
        time.sleep(60)

