class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self, head=None):
        self.head = head

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("La pila está vacía")
            return

        current_node = self.head
        self.head = current_node.next

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


def main():

    tercer_nodo = Node("Soy el tercer nodo")
    segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
    primer_nodo = Node("Soy el primer nodo", segundo_nodo)

    stack = Stack(primer_nodo)

    print("Pila inicial:")
    stack.print_structure()

    print("\nAgregando un elemento:")
    stack.push(Node("Soy el nuevo nodo!"))
    stack.print_structure()

    print("\nQuitando un elemento:")
    stack.pop()
    stack.print_structure()


if __name__ == "__main__":
    main()