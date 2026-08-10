import csv

def get_videogames():

    videogames = []

    number_of_games = int(input("¿Cuántos juegos desea incluir? "))

    for i in range(number_of_games):

        print(f"\nVideojuego #{i + 1}")

        game = {}

        game["nombre"] = input("Digite el nombre del juego: ")
        game["genero"] = input("Digite el género del juego: ")
        game["desarrollador"] = input("Digite el desarrollador del juego: ")
        game["clasificacion"] = input("Digite la clasificación ESRB del juego: ")

        videogames.append(game)

    return videogames


def save_videogames(file_path, data):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, dialect = 'excel-tab')

        writer.writeheader()

        writer.writerows(data)


def main():

    videogames = get_videogames()
    save_videogames("games.csv", videogames)

if __name__ == "__main__":
    main()