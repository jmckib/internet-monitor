import re
import subprocess
import time
import traceback

import requests

SLEEP_TIME = 60 * 60  # one hour in seconds
RECORD_SPEED_URL = 'http://negev-wifi-uptime.herokuapp.com/record-speed/'


def main():
    while True:
        try:
            output = subprocess.check_output(
                ['speedtest-cli'],
                stderr=subprocess.STDOUT)
        except:
            traceback.print_exc()
            time.sleep(SLEEP_TIME)
            continue

        # get download speed from wget output
        output_match = re.search(r'Download: ([0-9.]+ [KM]bit/s)', output)
        if not output_match:
            print output
            time.sleep(SLEEP_TIME)
            continue

        speed_str, units = output_match.group().split()[1:]
        speed = float(speed_str)

        # Convert to Kilobyte/s
        if units == 'Mbit/s':
            speed *= 125
        elif units == 'Kbit/s':
            speed *= 0.125
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
