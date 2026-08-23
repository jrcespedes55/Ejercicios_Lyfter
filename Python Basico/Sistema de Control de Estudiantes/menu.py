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
    return int(input("Select an option on the Menu: "))


def run_menu(answer):
    match answer:
        case 1:
            students = Data.data.read_students("Data/students.csv")
            new_students = actions.add_students()

            for student in new_students:
                students.append(student)
            Data.data.save_students("Data/students.csv", students)

        case 2:
            students = Data.data.read_students("Data/students.csv")
            actions.print_students(students)

        case 3:
            students = Data.data.read_students("Data/students.csv")
            actions.top_three_students(students)

        case 4:
            students = Data.data.read_students("Data/students.csv")
            actions.general_grades_average(students)

        case 5:
            students = Data.data.read_students("Data/students.csv")
            Data.data.export_students_data(students)

        case 6:
            students = Data.data.import_students_data("students.csv")
            actions.print_students(students)

        case 0:
            print("Exit the system")

        case _:
            print("Option not valid, try again.\n")