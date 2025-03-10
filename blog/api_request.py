import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('author', 'fhaskjbniuweiyGOIG12'))
pprint(response.json())