class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def print_structure(self, node, level=0):

        if node is None:
            return

        print("  " * level + str(node.data))

        self.print_structure(node.left, level + 1)
        self.print_structure(node.right, level + 1)


def main():

    tree = BinaryTree()

    tree.root = Node("A")

    tree.root.left = Node("B")
    tree.root.right = Node("C")

    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")

    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")

    tree.print_structure(tree.root)

if __name__ == "__main__":
    main()