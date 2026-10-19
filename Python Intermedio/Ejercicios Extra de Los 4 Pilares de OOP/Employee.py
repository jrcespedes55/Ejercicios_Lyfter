class Employee:

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    def promote(self, percentage):
        self.salary = self.salary * (1 + percentage)


def main():

    try:
        employee = Employee("Ana", 1000)

        print(f"The salary of {employee.name} = {employee.salary}")

        employee.promote(0.1)

        print(f"The new salary of {employee.name} = {employee.salary}")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()