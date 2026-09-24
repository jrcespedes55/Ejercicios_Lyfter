import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return  math.pi * (self.radius ** 2)


def main():

    my_first_circle = Circle(4)
    my_second_circle2 = Circle(5)
    my_third_circle = Circle(6)
    print(my_first_circle.get_area())
    print(my_second_circle2.get_area())
    print(my_third_circle.get_area())

if __name__ == "__main__":
    main()