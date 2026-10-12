class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):

        if self.head is None:
            print("La lista está vacía")
            return

        # Si el nodo que queremos eliminar es el primero
        if self.head.data == data:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return

        # Buscar el nodo que contiene el dato
        previous_node = self.head
        current_node = self.head.next

        while current_node is not None:

            if current_node.data == data:
                previous_node.next = current_node.next

                # Si eliminamos el último nodo
                if current_node == self.tail:
                    self.tail = previous_node

                return

            previous_node = current_node
            current_node = current_node.next

        print(f"El valor {data} no existe en la lista")

    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()


def main():

    lista = LinkedList()

    print("Insertando al inicio:")
    lista.insert_front(10)
    lista.insert_front(20)
    lista.print_all()

    print("\nInsertando al final:")
    lista.insert_back(30)
    lista.print_all()

    print("\nEliminando el valor 10:")
    lista.delete(10)
    lista.print_all()

    print("\nInsertando otro valor al final:")
    lista.insert_back(40)
    lista.print_all()

    print("\nEliminando el primer elemento, 20:")
    lista.delete(20)
    lista.print_all()

    print("\nEliminando el último elemento, 40:")
    lista.delete(40)
    lista.print_all()


main()