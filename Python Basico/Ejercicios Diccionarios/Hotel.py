print("---- Hotel ----\n")

hotel = {
	'name': 'Riu Palace',
	'number_stars': 4,
	'rooms': [
        {
            "room_number": 101,
            "floor": 1,
            "price_night": 80
        },
        {
            "room_number": 202,
            "floor": 2,
            "price_night": 120
        },
        {
            "room_number": 303,
            "floor": 3,
            "price_night": 150
        }
    ]
}
print("Nombre del hotel:", hotel["name"])
print("Número de estrellas:", hotel["number_stars"])
print("rooms:")

for room in hotel['rooms']:
    print(f"Habitación {room['room_number']} - Piso {room['floor']} - Precio: ${room['price_night']} por noche")
