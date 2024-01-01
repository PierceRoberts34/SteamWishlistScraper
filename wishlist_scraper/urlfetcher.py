import requests
import time

def grab_URL(url, parameters=None):
    # Try to query the url given
    grab = requests.get(url, params=parameters)
    if grab:
        return grab
    else:
        # Try again if no response
        print('No response, waiting 10 seconds...')
        time.sleep(10)
        print('Retrying.')
        return grab_URL(url, parameters)