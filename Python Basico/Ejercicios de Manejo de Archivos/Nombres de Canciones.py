def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def sort_songs(lines):
    # Quita espacios/saltos de línea y descarta líneas vacías
    songs = [line.strip() for line in lines if line.strip()]
    # Ordena alfabéticamente (ignorando mayúsculas/minúsculas)
    sorted_songs = sorted(songs, key=str.lower)
    return sorted_songs

def write_new_file(path, sorted_songs):
    with open(path, 'w', encoding='utf-8') as file:
        for song in sorted_songs:
            file.write(song + "\n")

def print_songs():
    print("Canciones Ordenadas: \n")
    with open('canciones_ordenadas.txt', 'r', encoding='utf-8') as file:
        songs = file.read()
    print(songs)

def main():
    path = 'canciones.txt'
    path_new_file = 'canciones_ordenadas.txt'
    lines = read_file_by_lines(path)
    sorted_songs = sort_songs(lines)
    write_new_file(path_new_file,sorted_songs)
    print_songs()

if __name__ == "__main__":
    main()