import requests
import config

def main():

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

    print(api_res.url)
    print(api_res.json())

main()