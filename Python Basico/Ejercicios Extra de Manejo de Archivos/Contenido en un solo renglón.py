def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def remove_lines(lines):
    # Quita espacios/saltos de línea y descarta líneas vacías
    one_line_text = " ".join(line.strip() for line in lines if line.strip())
    return one_line_text

def write_new_file(path, new_text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(new_text)
    print(f'Nuevo texto: {new_text}')

def main():
    path = 'text.txt'
    path_new_file = 'new_text.txt'
    lines = read_file_by_lines(path)
    one_line_text = remove_lines(lines)
    write_new_file(path_new_file, one_line_text)
    

if __name__ == "__main__":
    main()