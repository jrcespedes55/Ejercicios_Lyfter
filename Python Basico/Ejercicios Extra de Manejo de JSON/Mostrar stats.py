import json

def read_pokemon(path):
    with open(path, mode='r', encoding='utf-8') as file:
        pokemones = json.load(file)
    return pokemones



def print_pokemones(pokemones):
    if not pokemones:
        print("No se encontraron pokémon de ese tipo.")
        return

    for i, pokemon in enumerate(pokemones, start=1):
        print(f"\nPokémon #{i}")
        print(f"Nombre : {pokemon['name']}\n")
        #print(f"Estadísticas principales: {pokemon['stats']}")
        for key, value in pokemon['stats'].items():
            print(f"{key}: {value}")



def main():

    pokemones = read_pokemon('pokemones_stats.json')
    print_pokemones(pokemones)

if __name__ == "__main__":
    main()