import csv

def read_games(path):
    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        return list(csv_reader)

def ask_user():
    return input("Ingrese una clasificación ESRB:\n")

     
def filter_by_type(games, game_type):
    filtered = []

    for game in games:
        if game[3] == game_type:
            filtered.append(game)

    return filtered

def print_games(games):
    for game in games:
        print(f"Nombre: {game[0]}")
        print(f"Género: {game[1]}")
        print(f"Desarrollador: {game[2]}")
        print(f"Clasificación: {game[3]}")
        print()   # Saltar encabezados

def main():

    games = read_games('games.csv')
    game_type = ask_user()
    filtered_games = filter_by_type(games, game_type)
    print_games(filtered_games)

if __name__ == "__main__":
    main()