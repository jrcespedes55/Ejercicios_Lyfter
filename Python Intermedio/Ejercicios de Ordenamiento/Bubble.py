def bubble_sort(my_list):
    for times_sorted in range(len(my_list) - 1):
        for index in range(len(my_list) - 1):
            if my_list[index] > my_list[index + 1]:
                bubble = my_list[index + 1]
                my_list[index + 1] = my_list[index]
                my_list[index] = bubble


def starting_right_bubble_sort(my_list):
    for pass_number in range(len(my_list) - 1):
        for index in range(len(my_list) - 1, pass_number, -1):
            if my_list[index] < my_list[index - 1]:
                bubble = my_list[index - 1]
                my_list[index - 1] = my_list[index]
                my_list[index] = bubble


def main():
    my_list = [8, 6, 4, 7, 1]
    my_list2 = [10, 8, 2, 11, 2, 6, 4]
    bubble_sort(my_list)
    print(my_list)

    starting_right_bubble_sort(my_list2)
    print(my_list2)


if __name__ == "__main__":
    main()