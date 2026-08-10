import csv

def read_games(path):
    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)   # Saltar encabezados
        
        for row in csv_reader:
            print(f"Nombre: {row[0]}")
            print(f"Género: {row[1]}")
            print(f"Desarrollador: {row[2]}")
            print(f"Clasificación: {row[3]}")
            print()

def main():

    read_games('games.csv')

if __name__ == "__main__":
    main()

