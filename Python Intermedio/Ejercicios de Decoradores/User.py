from datetime import date


class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()

        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def adult_required(function):
    def wrapper(user):
        if user.age < 18:
            raise Exception("The user must be 18 years old or older.")

        return function(user)

    return wrapper


@adult_required
def access_restricted_content(user):
    print("Access granted!")

def main():

    try:
        my_user = User(date(2016, 2, 12))
        #my_user = User(date(2008, 2, 12))
        # my_user = User(date(1995, 2, 12))

        print(f"Age: {my_user.age}")
        access_restricted_content(my_user)

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()