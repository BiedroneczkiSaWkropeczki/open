import requests
import json
import random   # do przetestowania
from faker import Faker 


def generate_client_data():
    fake_data = Faker()
    client_name = fake_data.name()
    client_email = fake_data.email()
    print(client_name, client_email)
    client_data = {"clientName": client_name,
                   "clientEmail": client_email
                   }
    print(client_data)
    return client_data 

def get_request(url, headers=''):
    response = requests.request("GET", url, headers=headers)
    return response

def post_request(url):
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps(generate_client_data())
    print(f"PAYLOAD: {payload}")
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

get_result = get_request("https://simple-books-api.click")
post_result = post_request("https://simple-books-api.click/api-clients")

print(get_result.status_code, get_result.text)
print(post_result.status_code, post_result.text)

# Wydrukujemy sobie to w osobnej linijce
print(50 * "-")
print(post_result.text)

# Zrobmy z post_result.text slownik
data = post_result.json()
print(data['accessToken'])
print(type(data), type(post_result.text))
print(post_result.json()['accessToken'])
