from services.common_db import Connection
from services.darksky.darksky_services import request_darksky_data, write_met_to_db
from utils.constants import *


def main():

    conn = Connection(host='localhost', database=air_quality_dev_db)
    api_key = darksky_api_key

    location_table_name = los_angeles_epa_sensor_locations_table_name
    location_column_set = ['station_id', 'lon', 'lat']
    locations = conn.read(location_table_name, location_column_set, '')

    timestamp_table_name = los_angeles_epa_air_quality_table_name
    timestamp_column_set = ['DISTINCT(date_observed)']
    timestamps = conn.read(timestamp_table_name, timestamp_column_set,
                           'where date_observed >= \'2017-03-01\' and date_observed < \'2017-05-01\' order by date_observed')

    met_table_name = los_angeles_meterology_table_name

    time_list = [x[0].strftime('%Y-%m-%dT%H:%M:%S%Z:00') for x in timestamps]

    for timestamp in time_list:
        dk_models = []
        for loc in locations:
            dk_model = request_darksky_data(loc[0], loc[1], loc[2], timestamp, api_key)
            if dk_model is not None:
                dk_models.append(dk_model)
        write_met_to_db(met_table_name, dk_models, conn)

    conn.close_conn()


def main_utah():

    conn = Connection(host='localhost', database=air_quality_dev_db)
    api_key = darksky_api_key

    location_table_name = utah_purple_air_quality_table_name
    location_column_set = ['station_id', 'lon', 'lat']
    locations = conn.read(location_table_name, location_column_set, '')
    locations = list(set(locations))

    timestamp_table_name = utah_purple_air_quality_table_name
    timestamp_column_set = ['DISTINCT(date_observed)']
    timestamps = conn.read(timestamp_table_name, timestamp_column_set,
                           'where date_observed >= \'2017-10-01\' and date_observed < \'2018-07-01\' order by date_observed')

    met_table_name = utah_meterology_table_name

    time_list = [x[0].strftime('%Y-%m-%dT%H:%M:%S%Z:00') for x in timestamps]

    for timestamp in time_list:
        dk_models = []
        for loc in locations:
            dk_model = request_darksky_data(loc[0], loc[1], loc[2], timestamp, api_key)
            if dk_model is not None:
                dk_models.append(dk_model)
        write_met_to_db(met_table_name, dk_models, conn)

    conn.close_conn()

if __name__ == '__main__':
    # main()
    main_utah()