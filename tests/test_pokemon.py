import requests
import pytest

token = '8206509ee7581926705322c0c4365c2f'
host = 'https://api.pokemonbattle-stage.me:9101'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_name_trainer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1403})
    assert response.json()['trainer_name'] == 'Boss'
