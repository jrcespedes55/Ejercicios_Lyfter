def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def write_new_file(path, new_text):
    with open(path, 'w', encoding='utf-8') as file:
        for line in new_text:
            file.write(line.upper())

def main():
    path = 'lower_case.txt'
    path_new_file = 'upper_case.txt'
    new_text = read_file_by_lines(path)
    write_new_file(path_new_file, new_text)
    print(read_file(path_new_file))
    

if __name__ == "__main__":
    main()