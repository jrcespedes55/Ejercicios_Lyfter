def get_nodes_in_order(node, nodes):
    if node is None:
        return

    get_nodes_in_order(node.left, nodes)
    nodes.append(node)
    get_nodes_in_order(node.right, nodes)


def bubble_sort_tree(root):
    nodes = []
    get_nodes_in_order(root, nodes)

    iterations = 0
    swaps = 0
    size = len(nodes)

    for pass_number in range(size - 1):
        iterations += 1

        for index in range(size - 1 - pass_number):
            if nodes[index].data > nodes[index + 1].data:
                bubble = nodes[index].data
                nodes[index].data = nodes[index + 1].data
                nodes[index + 1].data = bubble
                swaps += 1

    return iterations, swaps