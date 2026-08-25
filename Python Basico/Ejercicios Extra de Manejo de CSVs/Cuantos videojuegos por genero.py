import csv

def read_games(path):
    genres = []
    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)   # Saltar encabezados
        for row in csv_reader:
            genres.append(row[1])
    return genres


def count_genres(genres):
    my_dictionary = {}

    for genre in genres:
        if genre in my_dictionary:
            my_dictionary[genre] += 1
        else:
            my_dictionary[genre] = 1

    return my_dictionary
           
        

def print_games(dictionary):
    print("Géneros encontrados:")
    for genre, valor in dictionary.items():
        print(f"{genre}: {valor}")


def main():

    genres = read_games('games.csv')
    my_dictionary = count_genres(genres)
    print_games(my_dictionary)

if __name__ == "__main__":
    main()