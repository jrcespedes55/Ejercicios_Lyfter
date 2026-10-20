from Ejercicios_de_Estructuras_de_Datos.Stack import Node as StackNode, Stack
from Ejercicios_Extra_de_Ordenamiento.Bubble_sort import bubble_sort_linked
from Ejercicios_de_Estructuras_de_Datos.Deque import Node as DequeNode, Deque

from Ejercicios_de_Estructuras_de_Datos.BinaryTree import (
    Node as TreeNode,
    BinaryTree
)
from Ejercicios_Extra_de_Ordenamiento.Bubble_sort_tree import bubble_sort_tree


def main():
    stack = Stack()

    stack.push(StackNode(5))
    stack.push(StackNode(2))
    stack.push(StackNode(4))
    stack.push(StackNode(1))
    stack.push(StackNode(3))

    print("===== STACK =====")
    print("Antes de ordenar:")
    stack.print_structure()

    iterations, swaps = bubble_sort_linked(stack.head)

    print("\nDespués de ordenar:")
    stack.print_structure()
    print("Iteraciones:", iterations)
    print("Intercambios:", swaps)

    # Prueba del Deque
    deque = Deque()

    deque.push_right(DequeNode(5))
    deque.push_right(DequeNode(2))
    deque.push_right(DequeNode(4))
    deque.push_right(DequeNode(1))
    deque.push_right(DequeNode(3))

    print("\n===== DEQUE =====")
    print("Antes de ordenar:")
    deque.print_structure()

    iterations, swaps = bubble_sort_linked(deque.head)

    print("\nDespués de ordenar:")
    deque.print_structure()
    print("Iteraciones:", iterations)
    print("Intercambios:", swaps)



    # Prueba del BinaryTree
    tree = BinaryTree()

    tree.root = TreeNode(7)
    tree.root.left = TreeNode(3)
    tree.root.right = TreeNode(6)

    tree.root.left.left = TreeNode(5)
    tree.root.left.right = TreeNode(1)

    tree.root.right.left = TreeNode(4)
    tree.root.right.right = TreeNode(2)

    print("\n===== BINARY TREE =====")
    print("Antes de ordenar:")
    tree.print_structure(tree.root)

    iterations, swaps = bubble_sort_tree(tree.root)

    print("\nDespués de ordenar:")
    tree.print_structure(tree.root)
    print("Iteraciones:", iterations)
    print("Intercambios:", swaps)

if __name__ == "__main__":
    main()