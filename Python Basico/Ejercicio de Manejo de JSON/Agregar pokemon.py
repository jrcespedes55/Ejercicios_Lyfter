import json


def read_pokemon(path):
    with open(path, mode='r', encoding='utf-8') as file:
        pokemones = json.load(file)
    return pokemones


def get_new_pokemon():
    name = input("Ingrese el nombre del Pokémon: ")
    hp = int(input("Ingrese el HP: "))
    pokemon_type = input("Ingrese el tipo: ")

    nuevo_pokemon = {
        "name": name,
        "hp": hp,
        "type": pokemon_type
    }

    return nuevo_pokemon


def add_pokemon(path, pokemones, nuevo_pokemon):
    pokemones.append(nuevo_pokemon)

    with open(path, mode='w', encoding='utf-8') as file:
        json.dump(pokemones, file, indent=4, ensure_ascii=False)


def main():
    path = "pokemones.json"

    pokemones = read_pokemon(path)
    nuevo_pokemon = get_new_pokemon()
    add_pokemon(path, pokemones, nuevo_pokemon)

    print("Pokémon agregado correctamente.")


if __name__ == "__main__":
    main()