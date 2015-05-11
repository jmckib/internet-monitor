import os
import time
import traceback

import requests


SLEEP_TIME = 20  # seconds
RECORD_PING_URL = 'http://negev-wifi-uptime.herokuapp.com/record-ping/'


def main():
    while True:
        response = os.system('ping -c 1 -w 2 google.com > /dev/null')

        if response == 0:
            try:
                response = requests.post(RECORD_PING_URL)
                print response
            except:
                traceback.print_exc()
        else:
            print 'DOWN'

        time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    main()
