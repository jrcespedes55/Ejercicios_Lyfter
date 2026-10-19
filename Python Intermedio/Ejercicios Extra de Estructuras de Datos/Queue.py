class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:

    def __init__(self, head=None):
        self.head = head

    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            print("La cola está vacía")
            return None

        current_node = self.head
        self.head = self.head.next

        return current_node.data

    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()


def main():
    queue = Queue()

    print("Agregando elementos:")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    queue.print_all()

    print("\nEliminando el primer elemento:")
    removed = queue.dequeue()
    print("Elemento eliminado:", removed)

    print("\nCola después de eliminar:")
    queue.print_all()

if __name__ == "__main__":
    main()