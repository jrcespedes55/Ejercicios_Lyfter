print("---- Sumar Valores ----\n")

def sum_of_values(list):
    total = 0
    for record in list:
        try:
            number = float(record)
            total += number
            print(f"'{number}' sumado correctamente")
        except ValueError:
            print(f"Elemento inválido: {record}")   
    return total  

def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    result = sum_of_values(my_list)
    print(f"Total de la suma: {result}")


if __name__ == '__main__':
        main()