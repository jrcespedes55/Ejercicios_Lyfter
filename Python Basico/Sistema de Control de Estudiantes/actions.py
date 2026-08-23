import re


def is_valid_name(name):
    if not name.strip():
        return False

    return not any(character.isdigit() for character in name)


def is_valid_section(section):
    pattern = r"^\d{2}[A-Za-z]$"
    return re.match(pattern, section.strip()) is not None


def is_valid_grade(grade):
    try:
        grade = int(grade)
        return 0 <= grade <= 100
    except ValueError:
        return False


def student_exists(students, name, section):
    for student in students:
        if (
            student["name"].strip().lower() == name.strip().lower()
            and student["section"].strip().upper() == section.strip().upper()
        ):
            return True

    return False


def get_valid_name():
    while True:
        name = input("Full Name: ").strip()

        if is_valid_name(name):
            return name

        print("Invalid name. The name cannot be empty or contain numbers.")


def get_valid_section():
    while True:
        section = input("Section: ").strip().upper()

        if is_valid_section(section):
            return section

        print("Invalid section. Use a format such as 10A or 11B.")


def get_valid_grade(subject):
    while True:
        grade = input(f"{subject} grade: ")

        if is_valid_grade(grade):
            return int(grade)

        print("Invalid grade. Enter a number between 0 and 100.")


def add_students(existing_students):
    students = []

    while True:
        try:
            number_of_students = int(
                input("How many students do you want to add? ")
            )

            if number_of_students > 0:
                break

            print("Enter a number greater than 0.")

        except ValueError:
            print("Invalid number. Enter a whole number.")

    for i in range(number_of_students):

        print(f"\n-> Student #{i + 1}")

        while True:
            name = get_valid_name()
            section = get_valid_section()

            if student_exists(existing_students + students, name, section):
                print("A student with that name and section already exists.")
                print("Please enter the information again.")
            else:
                break

        student = {
            "name": name,
            "section": section,
            "spanish": get_valid_grade("Spanish"),
            "english": get_valid_grade("English"),
            "social": get_valid_grade("Social Studies"),
            "science": get_valid_grade("Science")
        }

        students.append(student)

    return students


def print_students(students):
    if not students:
        print("There are no students to display.")
        return

    for student in students:
        print(f"\nFull Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish grade: {student['spanish']}")
        print(f"English grade: {student['english']}")
        print(f"Social grade: {student['social']}")
        print(f"Science grade: {student['science']}")
        print()


def student_grades_average(spanish, english, social, science):
    return (spanish + english + social + science) / 4


def general_grades_average(students):
    if not students:
        print("There are no students to display.")
        return

    for student in students:
        average = student_grades_average(
            student["spanish"],
            student["english"],
            student["social"],
            student["science"]
        )

        print(f"\nFull Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish grade: {student['spanish']}")
        print(f"English grade: {student['english']}")
        print(f"Social Studies grade: {student['social']}")
        print(f"Science grade: {student['science']}")
        print("-------------------------")
        print(f"Average: {average:.2f}")
        print()


def top_three_students(students):
    if not students:
        print("There are no students to display.")
        return

    students_with_average = []

    for student in students:
        average = student_grades_average(
            student["spanish"],
            student["english"],
            student["social"],
            student["science"]
        )

        student_copy = student.copy()
        student_copy["average"] = average
        students_with_average.append(student_copy)

    students_with_average.sort(
        key=lambda student: student["average"],
        reverse=True
    )

    print("\n===== Top 3 Students =====")

    for student in students_with_average[:3]:
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Average: {student['average']:.2f}")
        print("--------------------")

