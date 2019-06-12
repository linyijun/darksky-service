import pandas as pd
import pytz

from methods.request_data import request_target_locations
from methods.run_darksky_service import multiple_times_request
from utils.constants import LOS_ANGELES


def main(config):

    # Get target locations
    res = request_target_locations(config['TARGET_LOC'])
    loc_dict = res['data'] if res['status'] == 1 else exit(0)

    # From time to time request
    start_time = '2018-11-01 00:00:00'
    end_time = '2018-11-02 00:00:00'
    tz = pytz.timezone('America/Los_Angeles')
    time_list = pd.date_range(start=start_time, end=end_time, closed='left', freq='1H')
    time_list = [tz.localize(x).strftime('%Y-%m-%dT%H:%M:%S%z') for x in time_list]

    # Create DarkSky table

    # Request Darksky data and store in the database
    multiple_times_request(time_list, loc_dict, config)


if __name__ == '__main__':
    # main(BEIJING)
    main(LOS_ANGELES)