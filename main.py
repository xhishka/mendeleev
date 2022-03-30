import requests

url = 'http://api.forismatic.com/api/1.0/'
params = {'method': 'getQuote', 'key': '457653', 'format': 'json', 'lang': 'ru'}
result = requests.get(url, params=params)
quote = result.json()
print(quote["quoteText"])
print(quote["quoteAuthor"])
