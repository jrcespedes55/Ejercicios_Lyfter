print("---- Acumular Total por categoría ----\n")

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]


my_dictionary = {}

for product in products:
    category = product["category"]
    price = product["price"]

    my_dictionary[category] = my_dictionary.get(category, 0) + price

print(my_dictionary)