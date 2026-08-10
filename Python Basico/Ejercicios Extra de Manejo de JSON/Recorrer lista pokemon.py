import json

def read_pokemon(path):
    with open(path, mode='r', encoding='utf-8') as file:
        pokemones = json.load(file)
    return pokemones

def print_pokemones(pokemones):
    for i, pokemon in enumerate(pokemones, start=1):
        print(f"Pokémon #{i}")
        print(f"Nombre : {pokemon['name']}")
        print(f"HP     : {pokemon['hp']}")
        print(f"Tipo   : {pokemon['type']}\n")


def main():
    path = "pokemones.json"

    pokemones = read_pokemon(path)
    print_pokemones(pokemones)



if __name__ == "__main__":
    main()