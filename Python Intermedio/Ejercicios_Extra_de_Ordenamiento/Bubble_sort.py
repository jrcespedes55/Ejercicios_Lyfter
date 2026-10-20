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