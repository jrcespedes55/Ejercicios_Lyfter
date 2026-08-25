import random

print("---- Juego número secreto ----\n")

number = random.randint(1, 10)
guess = False

while(guess == False):
    number2 = int(input("Adivina un número del 1 al 10 \n"))
    if(number == number2):
        guess = True
    else:
        print("Intento incorrecto! \n")
    
print(f"Felicidades!!! Adivinaste el número secreto era: {number} ")