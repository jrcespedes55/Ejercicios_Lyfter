print("---- Cantidad de veces que aparece un elemento en una lista ----\n")

my_list = [4, 2, 7, 2, 8, 2, 1]
number_to_find = 2

times_found = 0
times_found_user = 0
list_size = 0
user_list = []
counter = 1

for record in my_list:
	if(record == number_to_find): 
		times_found = times_found + 1


print(f'El número {number_to_find} aparece {times_found} veces\n')
print("---- Ingresa una lista de números a tu gusto  ----\n")
print("---- Comencemos por el tamaño de la lista  ----\n")
list_size = int(input(f"De cuantos digitos desea la lista? \n")) 

while(counter <= list_size):
    number = int(input(f"Digite un número para la lista:  \n"))
    user_list.append(number)
    counter = counter + 1


number_to_find = int(input(f"\nAhora el número que queremos buscar:  \n"))
for record in user_list:
	if(record == number_to_find): 
		times_found_user = times_found_user + 1
		

print(f'El número {number_to_find} aparece {times_found_user} veces\n')