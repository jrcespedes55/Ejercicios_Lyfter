print("---- Números Positivos ----\n")

my_list = [3, 6, 0, -2, 4]
#my_list = [3, -6, 7, 2, 0]


counter = 0

for record in my_list:
	if(record <= 0):
		counter = counter + 1
	else:
		continue

if(counter > 0 ): 
        print("Hay al menos un número negativo o cero")
else:
	print("Todos los números de la lista son positivos")