class Calculator:

    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number


    def print_params(func):
        def wrapper(self, *args, **kwargs):
            print(
                f"Parameters: {self.first_number}, {self.second_number}"
            )

            result = func(self, *args, **kwargs)

            print(f"Return: {result}")

            return result

        return wrapper


    @print_params
    def sum(self):
        return self.first_number + self.second_number

def main():
    calculator = Calculator(5, 5)
    calculator.sum()


if __name__ == "__main__":
    main()