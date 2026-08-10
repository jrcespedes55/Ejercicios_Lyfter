print("---- Ordenar alfabéticamente ----\n")

text = "python-variable-funcion-computadora-monitor"
text2 = "zoey-yesenia-xinia-alba-brittiny-camila"
text3 = "carlos-francisco-daniel-ariel-ever-brayan"

my_list = []

def insert_words(text):
    word = ""
    for char in text:
        if char.isalpha():
            word += char
        else: 
            my_list.append(word)
            word = ""
    my_list.append(word)    #Sin esta linea no agrega a la lista una de las palabras


def sorting(list):
    list.sort()
    return list

def list_to_string(list):
    new_string = "-".join(list)
    return new_string

insert_words(text)
print(list_to_string(sorting(my_list)))

