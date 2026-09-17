class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = int(input("How much do you want to add to your account? \n"))
        self.balance += amount

    def withdraw(self):
        amount = int(input("How much do you want to subtract from your account? \n"))
        self.balance -= amount

    def show_bank_options(self):
        print("=== Lyfter National Bank\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Create Savings Account")
        print(f"0. Exit              Your account:    $ {self.balance}")

    def get_bank_option(self):
        while True:
            try:
                answer = int(input("Select an option: \n"))
                if 0 <= answer <= 3:
                    return answer
                print("Opción invalida.  (Usa 0 ... 3.)")
            except ValueError:
                print("Ingrese solo números.")


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance

    def withdraw(self):
        amount = int(input("How much do you want to withdraw?\n"))
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"You must maintain a minimum balance of ${self.min_balance}"
            )

        self.balance -= amount

def savings_menu(saving_account):

    while True:

        print("\n=== Savings Account ===")
        print(f"Balance: ${saving_account.balance}")
        print(f"Minimum balance: ${saving_account.min_balance}")
        print("1. Deposit")
        print("2. Withdraw")
        print("0. Back")

        try:
            option = int(input("Select an option:\n"))

            match option:

                case 1:
                    saving_account.deposit()

                case 2:
                    try:
                        saving_account.withdraw()
                    except ValueError as error:
                        print(error)

                case 0:
                    break

                case _:
                    print("Invalid option.")

        except ValueError:
            print("Enter only numbers.")



def main():

    bank_account = BankAccount()
    saving_account = None

    while True:

        bank_account.show_bank_options()
        answer = bank_account.get_bank_option()

        match answer:

            case 1:
                bank_account.deposit()

            case 2:
                bank_account.withdraw()

            case 3:
                min_balance = int(
                    input("Choose a minimum balance for your savings account:\n")
                )

                saving_account = SavingsAccount(min_balance)

                savings_menu(saving_account)

            case 0:
                break


if __name__ == "__main__":
    main()