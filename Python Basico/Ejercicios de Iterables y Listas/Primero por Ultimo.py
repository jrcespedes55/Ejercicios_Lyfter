print("---- Primer elemento por último elemento ----\n")

my_list = [4, 3, 6, 1, 7]
#my_list = [1,4, 3, 6, 1, 7,9]
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

number_elements = len(my_list) 
last_element = number_elements -1

deleted_item = my_list.pop(0)
deleted_item2 = my_list.pop(last_element - 1)

my_list.insert(0, deleted_item2)
my_list.insert(number_elements, deleted_item)


print(my_list)