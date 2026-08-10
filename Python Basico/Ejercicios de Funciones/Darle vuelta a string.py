print("---- String al revés ----\n")


my_string = 'Hola mundo'
my_string2 = 'Pizza con piña'
my_string3 = 'AnitalavalatinA'

def string_backwards(string):
    record = ''
    number_characters = len(string) -1
    for index in range(number_characters,-1,-1):
        record = record + string[index]
    return record

print(string_backwards(my_string))