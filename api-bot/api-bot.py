import requests
import config
import json
import datetime
import time

def main():

# time.sleep(5) # delays for 5 seconds

# Regular season dates
# October 28, 2014 to April 15, 2015
#
# events ex:
# "https://erikberg.com/events.json?date=20130131&sport=nba"

    dates = []

    date = datetime.datetime(2014,10,27)

    # for i in range(170):
    for i in range(5):
        date += datetime.timedelta(days=1)
        formatted_date = date.strftime("%Y%m%d")
        dates.append(str(formatted_date))

# print(dates)


    headers = {
        'Authorization': 'Bearer ' + config.access_token,
        'User-agent': config.user_agent,
        'Content-Type': 'application/json'
    }
    
    host = 'erikberg.com'
    format = 'json'

    url_paths = {
        'sport': None,
        'method': 'events',
        'id': None,
    }

    payload = {
        'sport': 'nba',
        'date': '20130131'
    }

    def build_url(host, url_paths, format):
        path = '/'.join(filter(None, (url_paths['sport'], url_paths['method'], url_paths['id'])))
        url = 'https://' + host + '/' + path + '.' + format
        return url

    api_url = build_url(host, url_paths, format)

    api_res = requests.get(api_url, headers=headers, params=payload)

    plain_json_res = json.dumps(api_res.json())

    print(api_res.url)
    # print(plain_json_res)

    # f = open('test.js', 'a')

    # f.write(str(plain_json_res))
    # 

    def get_event_urls(events_date):

        payload[date] = dates.pop(0)

    while len(dates) > 0:
        payload['date'] = dates.pop(0)
        api_res = requests.get(api_url, headers=headers, params=payload)
        plain_json_res = json.dumps(api_res.json())
        print(api_res.url)
        time.sleep(1)
        print(plain_json_res)
        time.sleep(10)



main()