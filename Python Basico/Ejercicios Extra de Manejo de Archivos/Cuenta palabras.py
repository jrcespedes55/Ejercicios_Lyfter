def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def separate_words(text):
    words = text.split()
    return words

def main():
    path = 'words_counter.txt'
    text = read_file(path)
    words = separate_words(text)
    print("Cantidad de palabras:", len(words))
    

if __name__ == "__main__":
    main()