import requests
from pprint import pprint

""" Запрос через обычную авторизацию по логину-паролю
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('author', 'fhaskjbniuweiyGOIG12'))
pprint(response.json())
"""
# Запрос через авторизацию по токену
token = '3b745e41c06f534d64115ecb4b04b5be06548b74' # Создан командой python manage.py drf_create_token author
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers) # Запрос
pprint(response.json())