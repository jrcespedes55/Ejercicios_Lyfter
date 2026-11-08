def bubble_sort(my_list):
    if not isinstance(my_list, list):
        raise TypeError("El parámetro debe ser una lista")

    for times_sorted in range(len(my_list) - 1):
        for index in range(len(my_list) - 1 - times_sorted):
            if my_list[index] > my_list[index + 1]:
                bubble = my_list[index + 1]
                my_list[index + 1] = my_list[index]
                my_list[index] = bubble



def main():
    my_list = [8, 6, 4, 7, 1]
    bubble_sort(my_list)
    print(my_list)


if __name__ == "__main__":
    main()