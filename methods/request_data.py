import json
import requests

from utils.common_db import session


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


def request_target_locations(location_obj):

    results = session.query(location_obj).with_entities(*[location_obj.gid, location_obj.lon, location_obj.lat]).all()

    loc_dict = {}

    if not results:
        return {'status': -1, 'msg': 'No target locations.', 'data': loc_dict}
    else:
        for res in results:
            loc_dict[res.gid] = (res.lon, res.lat)
        return {'status': 1, 'msg': '', 'data': loc_dict}
