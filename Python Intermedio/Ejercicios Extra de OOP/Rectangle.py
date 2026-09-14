
class Rectangle:
    def __init__(self, width, height):
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
        
            if width < 0:
                print("Existe un valor negativo, los valores deben ser positivos")
                continue
            break 
        except ValueError:
            print("Solo enteros positivos")
    return width

def valid_height():
    while True:
        try:
            height = int(input("Ingrese la altura: "))
        
            if height < 0:
                print("Existe un valor negativo, los valores deben ser positivos")
                continue
            break 
        except ValueError:
            print("Solo enteros positivos")
    return height


def main():
    height = valid_height()
    width = valid_width()

    rectangle = Rectangle(width,height)
    print(f"\nEl área del rectángulo es de: {rectangle.get_area()} ") 
    print(f"El perímetro del rectángulo es de: {rectangle.get_perimeter()} ") 

if __name__ == "__main__":
    main()