print("---- Agrupar Empleados por Departamento ----\n")

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

my_dictionary = {}

for employee in employees:
    department = employee["department"]
    
    if department not in my_dictionary:
        my_dictionary[department] = []
    
    my_dictionary[department].append(employee)

print(my_dictionary)
