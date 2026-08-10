total_of_grades = 0
counter_of_grades = 1
current_grade = 0
number_of_approved_grades = 0
number_of_disapproved_grades = 0
approved_grades_average = 0
disapproved_grades_average = 0
total_of_grades_average = 0

print("---- Calculos de notas ----\n")
total_of_grades = int(input("Ingrese la cantidad de notas \n"))

while(counter_of_grades <= total_of_grades):
    current_grade = int(input(f"Ingrese la nota número: {counter_of_grades} \n"))
    if(current_grade < 70):
        number_of_disapproved_grades = number_of_disapproved_grades + 1
        disapproved_grades_average = disapproved_grades_average + current_grade
    else:
        number_of_approved_grades = number_of_approved_grades + 1
        approved_grades_average = approved_grades_average + current_grade

    total_of_grades_average = total_of_grades_average + (current_grade / total_of_grades)
    counter_of_grades = counter_of_grades + 1
if(disapproved_grades_average != 0): #Validación importante que encontré
    disapproved_grades_average = disapproved_grades_average / number_of_disapproved_grades
if(approved_grades_average != 0):    #Validación importante que encontré
    approved_grades_average = approved_grades_average / number_of_approved_grades
print(f"\nEl estudiante tiene esta cantidad de notas aprobadas: {number_of_approved_grades}\n" )
print(f"Este es el promedio de notas aprobadas: {approved_grades_average}\n" )
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {number_of_disapproved_grades}\n" )
print(f"Este es el promedio de notas desaprobadas: {disapproved_grades_average}\n" )
print(f"Este es el promedio total de notas: {total_of_grades_average}\n" )