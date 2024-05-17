from math import sqrt
A = int(input("Ingrese el término cuadrático: "))
B = int(input("Ingrese el término lineal: "))
C = int(input("Ingrese el tèrmino independiente:"))

determinant = sqrt((B**2) -(4*A*C))
root_1 = (-B + determinant)/(2*A)
root_2 = (-B - determinant)/(2*A)

print(f"Las raíces son: {root_1} y {root_2}" )