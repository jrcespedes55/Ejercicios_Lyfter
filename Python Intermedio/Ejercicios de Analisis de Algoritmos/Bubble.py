def bubble_sort(my_list):
    for times_sorted in range(len(my_list) - 1): # O(n)
        for index in range(len(my_list) - 1 - times_sorted):   # O(n²)
            if my_list[index] > my_list[index + 1]: # O(1)
                bubble = my_list[index + 1]      # O(1)
                my_list[index + 1] = my_list[index]    # O(1)
                my_list[index] = bubble    # O(1)



def main():
    my_list = [8, 6, 4, 7, 1]  # O(1)
    bubble_sort(my_list) # O(n²)
    print(my_list) # O(n)

    # --> El algoritmo completo es O(n²).


if __name__ == "__main__":
    main()