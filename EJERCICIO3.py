#Cálculo de IMC
weight = float(input("Insert Weight (kg):") )
height = float(input("Insert Height (m):"))
imc = weight/(height)**2
print("Your IMC is: " , "{:.3f}".format(imc))

