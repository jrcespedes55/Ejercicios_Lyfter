def check_numbers(function):
    def wrapper(first_number, second_number):

        if not isinstance(first_number, (int, float)):
            raise TypeError("First parameter must be a number")

        if not isinstance(second_number, (int, float)):
            raise TypeError("Second parameter must be a number")

        return function(first_number, second_number)

    return wrapper


@check_numbers
def sum_numbers(first_number, second_number):
    return first_number + second_number


def main():

    try:
        print(sum_numbers(5, 10))
        print(sum_numbers(5, "10"))

    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()