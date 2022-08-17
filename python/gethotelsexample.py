import requests

# 500 free calls per month :\
url = 'https://hotels4.p.rapidapi.com/locations/v2/search'
headers = {
  'x-rapidapi-host': 'hotels4.p.rapidapi.com',
  'x-rapidapi-key': '748ac67f3cmshf3e99f25f444fd0p1d75ebjsn397e2d620ed4'
  }
params = {'query': 'san jose', 'locale': 'en_US', 'currency': 'USD'}

x = requests.get(url, headers=headers, params=params)

print(x.json()['suggestions'][1])