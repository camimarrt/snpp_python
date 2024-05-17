import clasecalc
num1 = 0
num2 = 0
if __name__ == "__main__":
    casio = clasecalc.Calculadora()
    while True:
        print("---OPERACION---")
        print("1.Suma.")
        print("2.Resta.")
        print("3.Multiplicación.")
        print("4.División.")
        print("5.Potenciación.")
        operacion = int(input("Seleccione una operación:"))
        n1 = float(input("Ingrese el primer número:  "))
        n2 = float(input("Ingrese el segundo número:  "))        
        if operacion == 1:
            casio.set_numeros(n1,n2)
            print(f"La suma es: {casio.suma()}")
        elif operacion == 2:
            casio.set_numeros(n1,n2)
            print(f"La diferencia es: {casio.resta()}")            
        elif operacion == 3:
            casio.set_numeros(n1,n2)
            print(f"El producto es: {casio.mul()}")
        elif operacion ==4:
            casio.set_numeros(n1,n2)
            print(f"La división es: {casio.div()}")
        elif operacion ==5:
            casio.set_numeros(n1,n2)
            print(f"La potencia es: {casio.pot()}")
        else:
            print("Opción no válida. Intente de nuevo.")            