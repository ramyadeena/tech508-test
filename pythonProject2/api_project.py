import requests
import random

# 1. Get Pokémon data by name
def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 2. Get random Pokémon
def get_random_pokemon():
    random_id = random.randint(1, 151)  # First generation
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 3. Print Pokémon info
def print_pokemon_info(pokemon):
    print(f"\nName: {pokemon['name'].capitalize()}")
    print(f"HP: {pokemon['stats'][0]['base_stat']}")
    print(f"Attack: {pokemon['stats'][1]['base_stat']}")
    print(f"Defense: {pokemon['stats'][2]['base_stat']}")
    print(f"Speed: {pokemon['stats'][5]['base_stat']}")
    print(f"Ability: {pokemon['abilities'][0]['ability']['name']}")

# 4. Battle logic
def battle(pokemon1, pokemon2):
    stat_to_compare = 'attack'
    stat_index = {
        'hp': 0,
        'attack': 1,
        'defense': 2,
        'speed': 5
    }
    index = stat_index[stat_to_compare]

    p1_stat = pokemon1['stats'][index]['base_stat']
    p2_stat = pokemon2['stats'][index]['base_stat']

    print(f"\n{pokemon1['name'].capitalize()} {stat_to_compare.capitalize()}: {p1_stat}")
    print(f"{pokemon2['name'].capitalize()} {stat_to_compare.capitalize()}: {p2_stat}")

    if p1_stat > p2_stat:
        print(f"\n{pokemon1['name'].capitalize()} wins!")
    elif p2_stat > p1_stat:
        print(f"\n {pokemon2['name'].capitalize()} wins!")
    else:
        print("\n It's a tie!")

# 5. Main game
def main():
    print("Welcome to the Pokémon Battle Game!")

    user_input = input("Enter your Pokémon name (or press Enter for a random one): ").strip()

    if user_input:
        player_pokemon = get_pokemon_data(user_input)
        if not player_pokemon:
            print("Invalid Pokémon name. Exiting.")
            return
    else:
        player_pokemon = get_random_pokemon()

    cpu_pokemon = get_random_pokemon()

    print("\Your Pokémon:")
    print_pokemon_info(player_pokemon)

    print("\n CPU's Pokémon:")
    print_pokemon_info(cpu_pokemon)

    print("\nLet the battle begin!")
    battle(player_pokemon, cpu_pokemon)

if __name__ == "__main__":
    main()


