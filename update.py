#!/usr/bin/env python

import datetime
import sys

import requests

import database


URL = 'https://app.onzo.co.nz/nearby/-41.290777/174.7791503/2000.0'

database.Location.delete().where(
    database.Location.update < (datetime.datetime.now() -
        datetime.timedelta(minutes=30)) ).execute()

r = requests.get(URL)
if r.status_code != 200 and "data" not in r.json():
    print >>sys.stderr, "Couldn't update"
    sys.exit(1)

# Insert bike data into database
for bike in r.json()['data']:
    print bike

    bike_result, _ = database.Bike.get_or_create(onzo_bike_id=bike['producid'])

    bike_result.battery = bike['battery']
    bike_result.charge_voltage = bike['chargeVoltage']
    bike_result.create_time = bike['createTime']
    bike_result.icc_id = bike['iccid']
    bike_result.lock_id = bike['id']
    bike_result.is_lock = bike['isLock']
    bike_result.lock_type = bike['lockType']
    bike_result.l_status = bike['lstatus']
    bike_result.mac = bike['mac']
    bike_result.model_num = bike['modelNum']
    bike_result.p_signal = bike['psignal']
    bike_result.p_status = bike['pstatus']
    bike_result.speed = bike['speed']
    bike_result.unlock_times = bike['unlockedTimes']
    bike_result.update_time = bike['updateTime']
    bike_result.voltage = bike['voltage']

    bike_result.save()

    geo_result = database.Location(
        bike = bike_result,
        location_mode = bike['locationMode'],
        latitude = bike['latitude'],
        longitude = bike['longitude'],
        direction = bike['direction'],
        height = bike['height'],
        update = datetime.datetime.now()
    )
    geo_result.save()
