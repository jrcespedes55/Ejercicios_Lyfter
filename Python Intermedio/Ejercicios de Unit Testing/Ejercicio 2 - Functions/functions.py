# ---- String al revés ----

def string_backwards(string):
    record = ''
    number_characters = len(string) - 1

    for index in range(number_characters, -1, -1):
        record = record + string[index]

    return record


# ---- Suma de lista ----

def list_sum(my_list):
    index = 0
    result = 0

    while index < len(my_list):
        result = result + my_list[index]
        index = index + 1

    return result


# ---- Número de mayúsculas y minúsculas ----

def count_case_letters(text):
    uppercase = 0
    lowercase = 0

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    return uppercase, lowercase


# ---- Ordenar alfabéticamente ----

def sort_words_alphabetically(text):
    my_list = []

    word = ""

    for char in text:
        if char.isalpha():
            word += char
        else:
            my_list.append(word)
            word = ""

    my_list.append(word)

    my_list.sort()

    return "-".join(my_list)


# ---- Números primos de una lista ----

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def get_prime_numbers(my_list):
    new_list = []

    index = 0

    while index < len(my_list):
        if is_prime(my_list[index]):
            new_list.append(my_list[index])

        index += 1

    return new_list