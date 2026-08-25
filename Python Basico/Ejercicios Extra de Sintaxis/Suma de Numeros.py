print("---- Suma de Números----\n")
user_number = 0
counter = 1
sum = 0

user_number = int(input("Digite un número:  \n"))

while(counter <= user_number):
    sum = sum + counter
    counter = counter + 1

print(f"La suma es de: {sum} ")
