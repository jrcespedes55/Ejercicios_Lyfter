class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, new_node):

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def push_right(self, new_node):

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):

        if self.head is None:
            print("La estructura está vacía")
            return

        self.head = self.head.next

        if self.head is None:
            self.tail = None

    def pop_right(self):

        if self.head is None:
            print("La estructura está vacía")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current_node = self.head

        while current_node.next != self.tail:
            current_node = current_node.next

        self.tail = current_node
        self.tail.next = None

    def print_structure(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


def main():

    deque = Deque()

    print("Agregando A a la derecha")
    deque.push_right(Node("A"))

    print("Agregando B a la derecha")
    deque.push_right(Node("B"))

    print("Agregando C a la izquierda")
    deque.push_left(Node("C"))

    print("\nEstructura:")
    deque.print_structure()

    print("\nQuitando elemento de la izquierda")
    deque.pop_left()

    deque.print_structure()

    print("\nQuitando elemento de la derecha")
    deque.pop_right()

    deque.print_structure()


main()