print("---- Diez números ----\n")

my_list = []
counter = 1
bigger_number = 0
while(counter <= 10):
    number = int(input(f"Digite el número: {counter}  \n"))
    my_list.append(number)
    if(number >= bigger_number):
        bigger_number = number
    counter = counter + 1


print(f"Sus números fueron: {my_list} ")
print(f"Y el número mayor es: {bigger_number}")