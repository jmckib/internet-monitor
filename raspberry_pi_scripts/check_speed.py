import re
import subprocess
import time
import traceback

import requests

SLEEP_TIME = 60 * 60  # one hour in seconds
RECORD_SPEED_URL = 'http://negev-wifi-uptime.herokuapp.com/stats/record-speed/'


def main():
    while True:
        # Download 10MB file
        try:
            output = subprocess.check_output(
                ['wget', '-O', '/dev/null',
                 'http://speedtest.wdc01.softlayer.com/downloads/test10.zip'],
                stderr=subprocess.STDOUT)
        except:
            traceback.print_exc()
            time.sleep(SLEEP_TIME)
            continue

        # get download speed from wget output
        output_match = re.search(r'([0-9.]+ [KM]B/s)', output)
        if not output_match:
            print output
            time.sleep(SLEEP_TIME)
            continue

        speed_str, units = output_match.group().split()
        speed = float(speed_str)

        # Convert to KB/s
        if units == 'MB/s':
            speed *= 1000
        speed = int(speed)  # dont need fractional kb

        # upload speed to website
        try:
            response = requests.post(RECORD_SPEED_URL,
                                     data={'kb_per_second': speed})
            print response
        except:
            traceback.print_exc()

        time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    main()
