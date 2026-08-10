print("---- Eliminar impares ----\n")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#my_list = [13, 22, 35, 42, 55, 62, 77, 80, 99]
#my_list = [13, 2, 35, 55, 77, 99]


my_flag = True

while(my_flag == True):
    my_flag = False
    for index in range(0,len(my_list)):
        if my_list[index] % 2 != 0:
            my_list.pop(index)
            my_flag = True
            break
        else:
            continue

print(my_list)
        