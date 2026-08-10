print("---- String de ederecha a izquierda ----\n")

my_string = 'Pizza con piña'
number_characters = len(my_string) -1

for index in range(number_characters,-1,-1):
	record = my_string[index]
	print(record)