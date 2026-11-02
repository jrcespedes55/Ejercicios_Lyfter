def bubble_sort_linked(head):
    iterations = 0
    swaps = 0

    if head is None:
        return iterations, swaps

    # Contar los nodos
    current_node = head
    size = 0

    while current_node is not None:
        size += 1
        current_node = current_node.next

    # Ordenar los nodos
    for pass_number in range(size - 1):
        iterations += 1
        current_node = head

        for index in range(size - 1 - pass_number):
            if current_node.data > current_node.next.data:
                bubble = current_node.data
                current_node.data = current_node.next.data
                current_node.next.data = bubble
                swaps += 1

            current_node = current_node.next

    return iterations, swaps


def bubble_sort(my_list):

    for pass_number in range(len(my_list) - 1):

        for index in range(len(my_list) - 1 - pass_number):

            if my_list[index] > my_list[index + 1]:
                bubble = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = bubble

    return my_list


def validated_bubble_sort(my_list):

    if len(my_list) == 0:
        return "Error: La lista está vacía"

    for element in my_list:
        if not isinstance(element, (int, float)) or isinstance(element, bool):
            return "Error: La lista contiene elementos no numéricos"

    return bubble_sort(my_list)
