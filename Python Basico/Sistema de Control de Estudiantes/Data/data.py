import csv

def save_students(file_path, students):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = students[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        writer.writerows(students)


def read_students(path):
    with open(path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        return list(csv_reader)