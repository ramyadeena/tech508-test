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
