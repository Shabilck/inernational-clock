import datetime
import pytz
import time

time_zones = [
    'America/New_York',
    'Europe/London',
    'Europe/Paris',
    'Asia/Tokyo',
    'Australia/Sydney'
]

while True:
    current_time = datetime.datetime.now()

    for time_zone in time_zones:
        tz = pytz.timezone(time_zone)
        localized_time = current_time.astimezone(tz)
        time_str = localized_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        print(f'{time_zone}: {time_str}')

    time.sleep(1)