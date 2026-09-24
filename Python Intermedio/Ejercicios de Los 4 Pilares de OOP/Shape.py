from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("El radio no puede ser negativo")

        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):

    def __init__(self, width, height):
        if width < 0:
            raise ValueError("El ancho no puede ser negativo")

        if height < 0:
            raise ValueError("La altura no puede ser negativa")

        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):

    def __init__(self, side):
        if side < 0:
            raise ValueError("El lado no puede ser negativo")

        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2

def main():

    while True:

        print("\n===== SHAPES =====")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("0. Exit")

        try:
            option = int(input("Choose a shape: "))

            match option:

                case 1:
                    radius = float(input("Enter the radius: "))
                    shape = Circle(radius)

                case 2:
                    side = float(input("Enter the side: "))
                    shape = Square(side)

                case 3:
                    width = float(input("Enter the width: "))
                    height = float(input("Enter the height: "))
                    shape = Rectangle(width, height)

                case 0:
                    break

                case _:
                    print("Invalid option.")
                    continue

            print(f"\nArea: {shape.calculate_area():.2f}")
            print(f"Perimeter: {shape.calculate_perimeter():.2f}")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()