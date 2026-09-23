import requests

def fetch_shop(url):
    res = requests.get(url)
    data = res.json()
    return data