
def repeat_twice(function):
    def wrapper(name):
        function(name)
        function(name)

    return wrapper


@repeat_twice
def print_name(name):
    print(f"Hola, {name}")


def main():
    print_name("Jose")


if __name__ == "__main__":
    main()