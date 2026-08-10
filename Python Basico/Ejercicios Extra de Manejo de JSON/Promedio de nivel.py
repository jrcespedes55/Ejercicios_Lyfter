import json

def read_pokemon(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def group_by_type(pokemones):
    grouped = {}
    for pokemon in pokemones:
        # Lee el tipo directamente del JSON
        type = pokemon["type"]
        
        # Lee el nivel directamente
        level = float(pokemon["level"])
        
        if type not in grouped:
            grouped[type] = []
        grouped[type].append(level)

        
    return grouped

def print_averages(grouped):
    for type, levels in grouped.items():
        if levels:
            average = sum(levels) / len(levels)
            print(f"Tipo: {type} → Promedio de nivel: {average}")

def main():
    path = "pokemones.json"
    pokemones = read_pokemon(path)
    grouped = group_by_type(pokemones)
    print_averages(grouped)

if __name__ == "__main__":
    main()


