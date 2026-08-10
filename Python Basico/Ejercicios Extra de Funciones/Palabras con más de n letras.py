print("---- Palabras que tengan más de n letras ----\n")

my_list = ["cielo", "sol", "maravilloso", "día"]


def more_than_n_words(list):
    final_list = []
    index = 0
    min_character = int(input("Ingrese el numero de letras minimas en la palabra: \n"))
    while index < len(list):
        if len(list[index]) > min_character:
            final_list.append(list[index])
        index += 1
    return final_list


print(more_than_n_words(my_list))


