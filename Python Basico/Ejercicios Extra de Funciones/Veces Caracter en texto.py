print("---- Cuántas veces aparece un carácter en un texto ----\n")

text = "programacion"
times_visible = 0

print(f"El texto actual es: {text}\n")

def times_found(text):
    times = 0
    character = input("Ingrese el carácter que desea buscar:\n")
    for char in text:
        if char == character:
            times += 1
    return times


def times_found2(text):
    character = input("Ingrese el carácter que desea buscar:\n")
    times = text.count(character)
    return times


times_visible = times_found(text)
print(f"El caracter seleccionado se encuentra: {times_visible} veces en el texto")
