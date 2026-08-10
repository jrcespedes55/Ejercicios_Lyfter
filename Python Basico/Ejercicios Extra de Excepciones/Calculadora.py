print("---- Calculadora ----\n")

def sum(current_number, second_number):
    return current_number + second_number

def subtraction(current_number, second_number):
    return current_number - second_number

def multiply(current_number, second_number):
    return current_number * second_number

def division(current_number, second_number):
    try:
        return current_number / second_number
    except ZeroDivisionError as e:
        print(f"Error: División por cero. Detalles: {e}")
        return None

def main():
    try:
        current_number = int(input("\nIngrese un primer número \n"))    
        while(True):
            try:
                operation = int(input("\nIngrese que operacion desea realizar: \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Borrar resultado \n"))
                match operation:
                    case 1:
                        second_number = int(input("\nIngrese un segundo número para sumar \n"))
                        current_number = sum(current_number, second_number)
                        print(f"Resultado = {current_number}")
                        
                    case 2:
                        second_number = int(input("\nIngrese un segundo número para restar \n"))
                        current_number = subtraction(current_number, second_number)
                        print(f"Resultado = {current_number}")                       
                    case 3:
                        second_number = int(input("\nIngrese un segundo número para multiplicar \n"))
                        current_number = multiply(current_number, second_number)
                        print(f"Resultado = {current_number}")                       
                    case 4:
                        second_number = int(input("\nIngrese un segundo número para dividir \n"))
                        temp_variable = division(current_number, second_number)
                        if(temp_variable != None):
                            current_number = temp_variable
                        print(f"\nResultado = {current_number}")                     
                    case 5:
                        print("\nResultado borrado! \n")
                        current_number = 0
                        print(f"\nResultado = {current_number}")                     
                    case _:
                        print("\nEl número digitado no corresponde con ninguna de las operaciones disponibles\n")

            except ValueError as ex:
                print("Entrada inválida: Ingrese un número entero válido.\n")

    
    except ValueError as ex:
        print("Entrada inválida: Ingrese un número entero válido.\n")

if __name__ == '__main__':
    while(True): 
        main()
