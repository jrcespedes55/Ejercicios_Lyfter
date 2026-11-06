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