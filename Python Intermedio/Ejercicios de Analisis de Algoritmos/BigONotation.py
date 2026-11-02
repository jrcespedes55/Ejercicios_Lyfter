def print_numbers_times_2(numbers_list):
	for number in numbers_list:  # O(n))
		print(number * 2)  # O(1))
		

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:  # O(n)
		for element_b in list_b:  # O(n²)
			if element_a == element_b:  # O(1)
				print("At least one equal element")	  # O(1)
				return True  # O(1)
	print("No equal elements")		  # O(1)	
	return False   # O(1)


def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)    # O(1)
	for index in range(min(list_len, 10)):    # O(1)
		print(list_to_print[index])    # O(1)


def generate_list_trios(list_a, list_b, list_c):
	result_list = []   # O(1)
	for element_a in list_a:   # O(n)
		for element_b in list_b:   # O(n²)
			for element_c in list_c:   # O(n3)
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(1)
				
	return result_list  # O(1)



def main():
    my_list = [8, 6, 4, 7, 1]  # O(1)
    my_list_B = [5, 7, 6, 2, 3]  # O(1)
    my_list_C = [2, 1, 5, 0, 3]  # O(1)
    print(f"Original lists: A = {my_list} B = {my_list_B} C = {my_list_C} \n") # O(1)
    
    print(" -- Mutiply x2:  --")
    print_numbers_times_2(my_list) # O(n)
    # --> El algoritmo es O(n).

    print("\n -- Equal elements --\n")
    check_if_lists_have_an_equal(my_list, my_list_B) # O(n²)
	# --> El algoritmo es O(n²)
	
    print("\n -- Print 10 --")
    print_10_or_less_elements(my_list_B)   # O(1)
	# --> El algoritmo es O(1)

    print("\n -- Generate trio --")
    result_list = generate_list_trios(my_list, my_list_B, my_list_C) # O(n3)
    print(result_list)
	# --> El algoritmo es O(n3)

if __name__ == "__main__":
    main()