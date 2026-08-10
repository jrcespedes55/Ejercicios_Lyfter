print("---- Números Primos de una lista ----\n")

my_list = [1, 4, 6, 7, 13, 9, 67]
new_list = []

def list_sum(list):
    index = 0
    while (index < len(list)):
        if is_prime(list[index]) == True:
            new_list.append(list[index])
        index += 1
    return new_list
    
    
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
print(list_sum(my_list))