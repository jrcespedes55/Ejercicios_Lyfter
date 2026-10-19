
class Rectangle:
    def __init__(self, width, height):
        if width < 0:
            raise ValueError("El ancho no puede ser negativo")

        if height < 0:
            raise ValueError("La altura no puede ser negativa")

        self.width = width
        self.height = height

    def get_area(self):
        return  (self.width * self.height)

    def get_perimeter(self):
        return 2 * (self.width + self.height)


def valid_width():
    while True:
        try:
            width = int(input("Ingrese el ancho: "))
            break
        except ValueError:
            print("Solo enteros")

    return width


def valid_height():
    while True:
        try:
            height = int(input("Ingrese la altura: "))
            break
        except ValueError:
            print("Solo enteros")

    return height


def main():
    while True:
        height = valid_height()
        width = valid_width()

        try:
            rectangle = Rectangle(width, height)
            break
        except ValueError as error:
            print(error)

    print(f"\nEl área del rectángulo es de: {rectangle.get_area()}")
    print(f"El perímetro del rectángulo es de: {rectangle.get_perimeter()}")


if __name__ == "__main__":
    main()