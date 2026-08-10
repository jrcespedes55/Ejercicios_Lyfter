print("---- Mostrar valor más pequeño ----\n")

#my_list = [9, 4, 7, 1, 5]
my_list = [9, 4, 7, 8, 11, 2, 1, 5]

counter = 0
min_number = my_list[0]
while(counter < len(my_list)):
    if(my_list[counter] < min_number):
        min_number = my_list[counter]
    counter = counter + 1


print(f"Sus números fueron: {my_list} ")
print(f"Y el número menor es: {min_number}")