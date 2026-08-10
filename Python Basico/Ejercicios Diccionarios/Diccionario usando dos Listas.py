print("---- Creando diccionario usando dos listas ----\n")

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
my_dictionary = {}

index = 0
while (index < len(list_a)):
	record = list_a[index]
	record2 = list_b[index]
	my_dictionary[record] =  record2
	index += 1


print(my_dictionary)