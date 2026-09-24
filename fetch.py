import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv('API_URL')

def fetch_shop():
    res = requests.get(api_url)
    data = res.json()
    return data
