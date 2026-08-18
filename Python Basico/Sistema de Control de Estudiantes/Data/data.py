import csv


def save_students(file_path, students):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        headers = students[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(students)


def read_students(file_path):
    students = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": int(row["spanish"]),
                    "english": int(row["english"]),
                    "social": int(row["social"]),
                    "science": int(row["science"])
                }

                students.append(student)

    except FileNotFoundError:
        pass

    return students


