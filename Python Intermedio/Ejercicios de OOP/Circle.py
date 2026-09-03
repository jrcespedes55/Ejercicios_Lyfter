import math

class Circle:
    radius = 4

    def get_area(self):
        return  math.pi * (self.radius ** 2)


def main():

    my_circle = Circle()
    print(my_circle.get_area())

if __name__ == "__main__":
    main()