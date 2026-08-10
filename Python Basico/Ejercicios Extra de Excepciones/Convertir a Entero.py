print("---- Convertir a Entero ----\n")

def convert_to_integer(list):
    for record in list:
        try:
             word = int(record)
             print(f"'{record}' convertido a {word}")
        except ValueError as ex:
                print(f"No se pudo convertir el elemento: {record}\n")         

def main():
    my_list = ['4', 'hola', '10', '5.2']
    print("Resultado:\n")
    convert_to_integer(my_list)


if __name__ == '__main__':
        main()