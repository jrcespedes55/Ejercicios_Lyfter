print("---- Tabla de multiplicar personalizada ----\n")
counter = 1

number = int(input("Ingrese un número del 1 al 10: \n"))
while(counter < 13):
        result = number * counter
        print(f"{number} X {counter} = {result}")
        counter = counter + 1