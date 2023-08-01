import requests

token = '8206509ee7581926705322c0c4365c2f' # токен 
host = 'https://api.pokemonbattle-stage.me:9101' # хост 


'''response_new_pokemon = requests.post(f'{host}/pokemons', json = {
    
    "name": "boss1",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"

}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})

print(response_new_pokemon.json())'''

'''response_rename_pokemon = requests.put(f'{host}/pokemons', json ={
    "pokemon_id": "1533",
    "name": "newBoss1",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})

print(response_rename_pokemon.json())'''
                                       
response_catch_pokemon = requests.post(f'{host}/trainers/add_pokeball', json ={

    "pokemon_id": "1533"

}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})

print(response_catch_pokemon.json())