print("---- Suma de lista ----\n")

my_list = [4,6,2,29]

def list_sum(list):
    index = 0
    result = 0
    while (index < len(list)):
        result = result + list[index]
        index = index + 1 
    return result

print(list_sum(my_list))

