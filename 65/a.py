# request api data
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("data retrieval failed")

is_running = True
while is_running:
    pokemon_name = input("Enter pokemon name")
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"{pokemon_info['name']}")
        print(f"{pokemon_info['id']}")
        print(f"{pokemon_info['height']}")
        print(f"{pokemon_info['abilities']}")

    choice = input("Want to know about more pokemons? Y / N?")
    if(choice == 'n'):
        is_running = False