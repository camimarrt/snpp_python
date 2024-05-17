import os 
import time
def menu():
    print("Elija una opción:")
    print("1. Calculadora:")
    print("2.Ver mi IP:")   
    print("3.Administrador de tareas.")
    print("4.Apagar el equipo en cinco minutos.")
    print("5.Cancelar Apagado")
    print("0. Salir")
    option = int(input("Ingrese una opción: "))
    return option

while True:
    option = menu() 
    if option == 0:
        break
    elif option==1:
        print("Cargando...")
        time.sleep(2)
        os.system("calc")
    elif option==2:
        print("Cargando...")
        time.sleep(2)
        os.system("ipconfig")
    elif option==3:
        print("Cargando...")
        time.sleep(2)
        os.system("task.mgr")
    elif option==4:
        print("Cargando...")
        time.sleep(2)
        os.system("cls")
    elif option==5:
        print("Cargando...")
        time.sleep(2)
        os.system("cls")
    elif option < 0 or option > 5:
        print("Opción Inválida. Intente de nuevo.")

