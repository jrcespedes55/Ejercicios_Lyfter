import json

def read_pokemon(path):
    with open(path, mode='r', encoding='utf-8') as file:
        pokemones = json.load(file)
    return pokemones

def ask_user():
    return input("Ingrese el tipo de pokemon desea buscar(water,electric, grass, fire,etc):\n")

     
def filter_by_type(pokemones, pokemon_type):
    filtered = []

    for pokemon in pokemones:
        if pokemon["type"].lower() == pokemon_type.lower():
            filtered.append(pokemon)

    return filtered

def print_pokemones(pokemones):
    if not pokemones:
        print("No se encontraron pokémon de ese tipo.")
        return

    for i, pokemon in enumerate(pokemones, start=1):
        print(f"Pokémon #{i}")
        print(f"Nombre : {pokemon['name']}")
        print(f"HP     : {pokemon['hp']}")
        print(f"Tipo   : {pokemon['type']}")

def main():

    pokemones = read_pokemon('pokemones.json')
    pokemon_type = ask_user()
    filtered_pokemones = filter_by_type(pokemones,pokemon_type)
    print_pokemones(filtered_pokemones)

if __name__ == "__main__":
    main()