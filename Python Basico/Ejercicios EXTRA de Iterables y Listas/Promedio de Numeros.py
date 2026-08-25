print("---- Promedio de números y Mostrar números mayores ----\n")

my_list = [10, 20, 30, 40, 50]
#my_list = [25, 25, 25, 25]
#my_list = [50, 70, 78, 80, 20]

new_list = []
number_of_elements = len(my_list)
total_of_values = 0
average_of_values = 0

for record in my_list:
	total_of_values = total_of_values + record

average_of_values = total_of_values / number_of_elements

for record in my_list:
    if(record > average_of_values):
          new_list.append(record)

print(f"Sus números fueron: {my_list} \n")
print(f"El promedio de los números es: {average_of_values}\n")
print(f"\nEsta es la nueva lista con los números mayores al promedio: {new_list}\n")