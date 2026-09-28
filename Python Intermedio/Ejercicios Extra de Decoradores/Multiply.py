from datetime import datetime

def validate_numbers(function):
    def wrapper(first_number, second_number):

        if not isinstance(first_number, (int, float)):
            raise TypeError("First parameter must be a number")

        if not isinstance(second_number, (int, float)):
            raise TypeError("Second parameter must be a number")

        return function(first_number, second_number)

    return wrapper


def log_call(function):
    def wrapper(first_number, second_number):
        result = function(first_number, second_number)

        current_date = datetime.now()

        print(
            f"Function: Multiply - args: {first_number}, {second_number} - "
            f"[{current_date}] - Resultado: {result}"
        )

        return result

    return wrapper



@log_call
@validate_numbers
def multiply(first_number, second_number):
    return first_number * second_number


def main():
    #result = multiply(5, 5)
    result = multiply(3, 4)
    print(f"Resultado {result}")


if __name__ == "__main__":
    main()