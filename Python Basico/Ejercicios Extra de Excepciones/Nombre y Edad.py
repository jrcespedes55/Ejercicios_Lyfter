print("---- Nombre y Edad ----\n")

def ask_name():
    name = input("Ingrese un nombre:\n")
    return name

def ask_age():
    age = (input("Ingrese su edad:\n"))
    try:
        return int(age)
    except ValueError:("Número no valido")
    return None

def validate_name(name):
    if (name.isdigit()):
        raise ValueError("El nombre no puede ser un número.")
    return name

def show_name_age(name, age):
    print(f"Hola {name}, su edad es {age}")

def main():

    name = ask_name()
    try:
        validate_name(name)
    except ValueError as e:
        print(e)
        return
    
    age = ask_age()
    if(age == None):
        return

    show_name_age(name,age) 




if __name__ == '__main__':
    while(True): 
        main()