def print_parameters(function):
    def wrapper(first_number, second_number):
        print(f"Parameters: {first_number}, {second_number}")

        result = function(first_number, second_number)

        print(f"Return: {result}")

        return result

    return wrapper


@print_parameters
def sum_numbers(first_number, second_number):
    return first_number + second_number


def main():
    sum_numbers(5, 5)


if __name__ == "__main__":
    main()