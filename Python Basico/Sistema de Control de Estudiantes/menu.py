import actions
import Data.data


def show_menu():
    print("\n===== Student Management System =====\n")
    print("1. Add students")
    print("2. View students")
    print("3. View top 3 students")
    print("4. View general average")
    print("5. Export students")
    print("6. Import students")
    print("0. Exit")


def get_menu_option():
    while True:
        try:
            answer = int(input("Select an option on the Menu: "))

            if 0 <= answer <= 8:
                return answer

            print("Option not valid. Select a number from 0 to 6.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def run_menu(answer):
    students = Data.data.read_students("Data/students.csv")

    match answer:
        case 1:
            new_students = actions.add_students(students)

            students.extend(new_students)

            Data.data.save_students(
                "Data/students.csv",
                students
            )

        case 2:
            actions.print_students(students)

        case 3:
            actions.top_three_students(students)

        case 4:
            actions.general_grades_average(students)

        case 5:
            Data.data.export_students_data(students)

        case 6:
            imported_students = Data.data.import_students_data(
                "students.csv"
            )

            if imported_students:
                Data.data.save_students(
                    "Data/students.csv",
                    imported_students
                )

                print("Students imported successfully.")

        case 0:
            print("Exit the system")