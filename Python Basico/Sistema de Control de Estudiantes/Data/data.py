import csv


def save_students(file_path, students):
    headers = [
        "name",
        "section",
        "spanish",
        "english",
        "social",
        "science"
    ]

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(students)

# Reads all the students from a CSV file, creates dictionaries for students data
# and return a list. If there is no file it will let the user know.
def read_students(file_path):
    students = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                try:
                    student = {
                        "name": row["name"],
                        "section": row["section"],
                        "spanish": int(row["spanish"]),
                        "english": int(row["english"]),
                        "social": int(row["social"]),
                        "science": int(row["science"])
                    }

                    students.append(student)

                except (ValueError, KeyError):
                    print("A row in the CSV contains invalid data.")

    except FileNotFoundError:
        print("No student data file found.")

    return students

# Exports a CSV file to different directory.
def export_students_data(students):
    columns = ['Name', 'Section', 'Spanish', 'English', 'Social Studies', 'Science'] 

    with open('students.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
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


# Imports a CSV file to the 'Data' folder. 
# In this folder the file will be used for the system functions.
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



