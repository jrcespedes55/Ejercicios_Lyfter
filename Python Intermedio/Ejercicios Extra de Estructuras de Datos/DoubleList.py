class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def delete(self, data):
        current_node = self.head

        while current_node is not None:

            if current_node.data == data:

                # Si es el primer nodo
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    current_node.previous.next = current_node.next

                # Si es el último nodo
                if current_node == self.tail:
                    self.tail = current_node.previous
                else:
                    current_node.next.previous = current_node.previous

                return

            current_node = current_node.next

        print(f"El valor {data} no existe en la lista")

    def print_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()

    def print_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.previous is not None:
                print(" -> ", end="")

            current_node = current_node.previous

        print()


def main():

    lista = DoublyLinkedList()

    print("Agregando elementos al final:")
    lista.append("A")
    lista.append("B")
    lista.append("C")

    print("De inicio a fin:")
    lista.print_forward()

    print("De fin a inicio:")
    lista.print_backward()

    print("\nAgregando X al inicio:")
    lista.prepend("X")

    print("De inicio a fin:")
    lista.print_forward()

    print("De fin a inicio:")
    lista.print_backward()

    print("\nEliminando B:")
    lista.delete("B")

    print("De inicio a fin:")
    lista.print_forward()

    print("De fin a inicio:")
    lista.print_backward()


if __name__ == "__main__":
    main()