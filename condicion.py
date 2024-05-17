num1 = int(input("Ingrese un número:  "))
num2 = int(input("Ingrese otro número:  "))

if (num1 > num2): 
    print(f"{num1} es mayor que {num2}")
    if (num1 % 2 == 0 ):
        print("El numero 1 es par.")
    else: 
        print("El numero es impar.")
elif (num1 < num2): 
    print(f"{num2} es mayor que {num1}.")
    if (num2 % 2 == 0):
        print("El número es par.")
    else: 
        print("El número es impar.")
else:
    print("Los números ingresados son iguales")
    