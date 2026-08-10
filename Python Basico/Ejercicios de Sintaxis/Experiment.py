#1 string + string 
name = "Jose"
last_name = " Céspedes"
print (name + last_name)

#2 string + int
age = 31
print(f"{name} tiene una edad de: {age} años")

#3 int + string
friends = 2
print(f"Mr.{last_name} tiene {friends} amigos")

#4 list + list
first_grade = ["Jose", "Juan", "Pepe", "Oscar", "Ronald"]
second_grade = ["Luis", "Manuel", "Pedro", "Oliver", "Allan"]
#option a. 
#students = first_grade + second_grade
#print(students)
#option b.
print(f"Todos los estudiantes son: Primer grado: {first_grade} y Segundo grado {second_grade}")

#5 string + list
boss = "John Li"
employees = ["Carlos", "Jose", "Juan", "Olman", "Rolando"]
print(f"El jefe de la empresa es {boss} y sus empleados son: {employees}")

#6 float + int
weight = 80
height = 1.72
print(f"Jose pesa {weight} kilos y mide {height} centimetros")

#7 bool + bool 
# Schrödinger's cat
cat_alive = True
cat_dead = True
box_opened = False

while(box_opened == False):
    cat_alive = True
    cat_dead = True
    break
print(f"Esta el gato vivo? {cat_alive} Esta el gato muerto? {cat_dead}")