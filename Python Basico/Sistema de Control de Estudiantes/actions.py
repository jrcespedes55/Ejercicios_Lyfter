def add_students():
    students = []
    number_of_students = int(input("¿How many students do you want to add? "))

    for i in range(number_of_students):

        print(f"\n-> Student #{i + 1}")

        student = {}

        student["name"] = input("Full Name: ")
        student["section"] = input("Section:")
        student["spanish"] = int(input("Spanish grade:"))
        student["english"] = int(input("English grade: "))
        student["social"] = int(input("Social Studies grade: "))
        student["science"] = int(input("Science grade: "))

        students.append(student)

    return students   


def print_students(students):
    for student in students:
        print(f"\nFull Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish grade: {student['spanish']}")
        print(f"English grade: {student['english']}")
        print(f"Social grade: {student['social']}")
        print(f"Science grade: {student['science']}")
        print()



def student_grades_average(spanish,english,social,science):
    return (spanish + english + social + science) / 4


def general_grades_average(students):
    for student in students:
        print("Full Name: ", student["name"])
        print(f"Section: {student["section"]}")
        print(f"Spanish grade: {student["spanish"]}")
        print(f"English grade: {student["english"]}")
        print(f"Social Studies grade: {student["social"]}")
        print(f"Science grade: {student["science"]}")
        print("-------- ---------")
        average = student_grades_average(
            student["spanish"],
            student["english"],
            student["social"],
            student["science"]
        )
        print(f"Average: {average}")       
        print()     


def top_three_students(students):
    students_with_average = []

    for student in students:
        average = student_grades_average(student["spanish"], student["english"],
        student["social"], student["science"])

        student["average"] = average
        students_with_average.append(student)

    students_with_average.sort(key=lambda student: student["average"], reverse=True)

    counter = 0

    for student in students_with_average:
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Average: {student['average']}")
        print("--------------------")

        counter += 1

        if counter == 3:
            break

    