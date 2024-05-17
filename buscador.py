import os
def menu():
    print("------BUSCADOR------")
    print("1. Google.")
    print("2.Wikipedia.")
    print("0. Cerrar.")
    option = int(input("Elija un buscador:"))
    return option
def web_search():
    search = input("Buscar:")
    return search
while True:
    option = menu()
    if option != 0:
            while True:
                search = web_search()
                if option == 1 and search != "0":
                    os.system("start chrome https://www.google.com/search?q=" + f"{search}")
                elif option == 2 and search != "0":
                    os.system("start chrome https://es.wikipedia.org/wiki/" + f"{search}")
                    

                    
                    break
    else:
        print("bye")
        break
