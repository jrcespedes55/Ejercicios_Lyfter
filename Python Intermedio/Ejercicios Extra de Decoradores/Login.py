user_logged_in = False
#user_logged_in = True

def requires_login(function):
    def wrapper():
        if user_logged_in == True:
            function()
        else:
            raise ValueError("Usuario no autenticado")

    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario")


def main():

    try:
        view_profile()

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()