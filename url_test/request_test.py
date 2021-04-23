import requests

url = 'https://www.google.com'
resp = requests.get(url)

print(resp.text)