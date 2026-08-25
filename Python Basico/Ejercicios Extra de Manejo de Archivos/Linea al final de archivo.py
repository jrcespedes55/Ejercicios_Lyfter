def ask_user_text():
    return input("Add more text to an existing file or create one:\n")

def append_to_file(path, extra_text):
    with open(path, "a", encoding="utf-8") as file:
        file.write(extra_text.rstrip("\n") + "\n")


def main():
    path = 'linea_al_final3.txt'
    new_text = ask_user_text()
    append_to_file(path, new_text)
    

if __name__ == "__main__":
    main()