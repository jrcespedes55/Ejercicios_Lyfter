def add_students():
    students = []
    number_of_students = int(input("¿How many students do you want to add? \n"))

    for i in range(number_of_students):

        print(f"\Student #{i + 1}")

        student = {}

        student["name"] = input("Full Name: ")
        student["section"] = input("Section:")
        student["spanish"] = input("Spanish grade:")
        student["english"] = input("English grade: ")
        student["social"] = input("Social Studies grade: ")
        student["science"] = input("Science grade: ")

        students.append(student)

    return students   



def print_students(students):
    for student in students:
        print(f"\nFull Name: {student[0]}")
        print(f"Section: {student[1]}")
        print(f"Spanish grade: {student[2]}")
        print(f"English grade: {student[3]}")
        print(f"Social grade: {student[4]}")
        print(f"Science grade: {student[5]}")
        print() 