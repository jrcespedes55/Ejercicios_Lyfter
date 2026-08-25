print("---- Tipo de Persona según su edad ----\n")

name = str(input("Ingresa tu nombre: "))
last_name = str(input("Ingresa tu apellido: "))
age = int(input("Ingresa tu edad: "))

if (age == 0 or age < 4): 
    print(f"{name} {last_name} es un Bebé ")
elif (age < 12): 
    print(f"{name} {last_name} es un Niño ")
elif (age < 14): 
            print(f"{name} {last_name} es un Preadolescente ")
elif (age < 18): 
            print(f"{name} {last_name} es un Adulto Joven ")
elif (age < 65): 
            print(f"{name} {last_name} es un Adulto ")
else:
            print(f"{name} {last_name} es un Adulto Mayor ")

