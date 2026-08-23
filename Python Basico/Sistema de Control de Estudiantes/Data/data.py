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

def export_students_data(students):
    columnas = ['Name', 'Section', 'Spanish', 'English', 'Social Studies', 'Science'] 

    with open('students.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(columnas)
        for student in students:
            writer.writerow([
                student["name"],
                student["section"],
                student["spanish"],
                student["english"],
                student["social"],
                student["science"],
                ])

    print("¡Archivo CSV creado con éxito!")




def import_students_data(file_path):
    students = []

    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                student = {
                    "name": row["Name"],
                    "section": row["Section"],
                    "spanish": int(row["Spanish"]),
                    "english": int(row["English"]),
                    "social": int(row["Social Studies"]),
                    "science": int(row["Science"])
                }

                students.append(student)

    except FileNotFoundError:
        print("File does not exist. Probably not exported yet.")
    except ValueError:
        print("Invalid value in the CSV.")
    except KeyError:
        print("The CSV file has unexpected columns.")

    return students



