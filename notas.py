grades = []
suma = 0
gpa = 0
def add_grade(grade):
    grades.append(grade)
def comprobation(grade):
    if grade<1 or grade>5:
        return False
    else: 
        return True
for x in range(3):
    grade = float(input(f"Ingrese la nota {x+1} :"))
    while comprobation(grade) == False:
        print("Error. Intente de nuevo.")
        grade = float(input(f"Ingrese la nota {x+1} :"))
    grades.append(grade)
    suma += grades[x]
    gpa = suma/3
print(f"El promedio es: {(gpa)} ")
