import pandas as pd
import pytz

from methods.db_ops import *
from methods.run_darksky_service import multiple_times_request
from constants import *


def main(config):

    # Get target locations
    res = request_target_locations(config['TARGET_LOC'])
    loc_dict = res['data'] if res['status'] == 1 else exit(0)

    # From time to time request
    start_time = config['START_TIME']
    end_time = config['END_TIME']
    tz = pytz.timezone('America/Los_Angeles')
    time_list = pd.date_range(start=start_time, end=end_time, closed='left', freq='1H')
    time_list = [tz.localize(x).strftime('%Y-%m-%dT%H:%M:%S%z') for x in time_list]

    # Create DarkSky table
    create_darksky_table(config['DARKSKY_OBJ'])

    # Request Darksky data and store in the database
    multiple_times_request(time_list, loc_dict, config)


if __name__ == '__main__':

    # main(LOS_ANGELES)
    # main(UTAH)

    tmp = {
        1: ['2018-01-01 00:00:00', '2018-02-01 00:00:00', LosAngeles5000mGridMeoDarkSky201801],
        2: ['2018-02-01 00:00:00', '2018-03-01 00:00:00', LosAngeles5000mGridMeoDarkSky201802],
        3: ['2018-03-01 00:00:00', '2018-04-01 00:00:00', LosAngeles5000mGridMeoDarkSky201803],
        4: ['2018-04-01 00:00:00', '2018-05-01 00:00:00', LosAngeles5000mGridMeoDarkSky201804],
        5: ['2018-05-01 00:00:00', '2018-06-01 00:00:00', LosAngeles5000mGridMeoDarkSky201805],
        6: ['2018-06-01 00:00:00', '2018-07-01 00:00:00', LosAngeles5000mGridMeoDarkSky201806],
        7: ['2018-07-01 00:00:00', '2018-08-01 00:00:00', LosAngeles5000mGridMeoDarkSky201807],
        8: ['2018-08-01 00:00:00', '2018-09-01 00:00:00', LosAngeles5000mGridMeoDarkSky201808],
        9: ['2018-09-01 00:00:00', '2018-10-01 00:00:00', LosAngeles5000mGridMeoDarkSky201809],
        10: ['2018-10-01 00:00:00', '2018-11-01 00:00:00', LosAngeles5000mGridMeoDarkSky201810],
        12: ['2018-12-01 00:00:00', '2019-01-01 00:00:00', LosAngeles5000mGridMeoDarkSky201812]
    }

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]:
        data = LOS_ANGELES
        data['START_TIME'] = tmp[i][0]
        data['END_TIME'] = tmp[i][1]
        data['DARKSKY_OBJ'] = tmp[i][2]
        main(data)

