print("---- Número Mayor ----\n")
number1 = int(input("Ingresa el primer número \n"))
number2 = int(input("Ingresa el segundo número \n"))
number3 = int(input("Ingresa el tercer número \n"))
numbers = [number1, number2, number3]
bigger_number = numbers[0]

for i in numbers:
    if i > bigger_number:
        bigger_number = i

print(f"\nEl número mayor es:  {bigger_number}")