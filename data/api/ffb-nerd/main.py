import requests
import json

url = 'http://www.fantasyfootballnerd.com/service/players/json/test/TE/'
f = open('tes.js', 'w')

res = requests.get(url)

data = json.dumps(res.json())

f.write(data)

# print(data)


