class Person():
	def __init__(self):
		print("1 more passenger")

class Bus:

    def __init__(self):
        self.people = []
        self.max_passengers = 10

    def show_bus_options(self):
        print("\n===== Bus Options =====\n")
        print(f"Current passengers: {len(self.people)} / {self.max_passengers}") 
        print("1. Pick up a person")
        print("2. Get a passenger off")
        print("0. Exit")

    def get_bus_option(self):
        while True:
            try:
                answer = int(input("Select an option on the Menu: "))
                if 0 <= answer <= 2:
                    return answer
                print("Option not valid. Select a number from 0 to 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
    def get_on_the_bus(self, person):
        if len(self.people) < self.max_passengers:
            self.people.append(person) 
            print(f"Passenger is now on the bus!")
        else:
            print("The bus is full, try to get on the next one")

    def get_off_the_bus(self):
        if len(self.people) > 0:
            self.people.pop(0) 
            print("\nPassenger got off the bus.")
        else:
            print("\nThe bus is empty, no passengers yet")


def main():
    my_bus = Bus()

    while(True):
        my_bus.show_bus_options()
        answer = my_bus.get_bus_option()
        match answer:
            case 1:
                my_person = Person()
                my_bus.get_on_the_bus(my_person)
            case 2:
                my_bus.get_off_the_bus()
            case 0:
                break
    

if __name__ == "__main__":
    main()