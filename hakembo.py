import random
import os
def menu():
    print("---HAKEMBO---")
    print("1. Piedra.")
    print("2.Papel.")
    print("3.Tijera.")
    option= int(input("Elija su jugada:"))
    return option
while True:
    option = menu()
    aleatorio = random.randrange(0,3)
    if aleatorio == 0:
        pc = "Piedra"
    elif aleatorio == 1:
        pc = "Papel"
    elif aleatorio == 2:
        pc = "Tijera."
    print(f"La PC eligió:{pc}")
    if aleatorio == 0 and option == 1:
        print("Ganaste.")
    elif aleatorio== 1 and option== 1:
        print("Perdiste.")
    elif aleatorio == 1 and option ==3:
        print("Perdiste.")
    elif aleatorio == 2 and option ==1:
        print("Ganaste.")
    elif aleatorio == 1 and option ==3:
        print("Ganaste.")
    elif aleatorio == 2 and option ==2:
        print("Perdiste.")
    elif aleatorio == option:
        print("Empate.")

    play_again = input("Quieres jugar de nuevo? (Si/No):  ")
    if play_again == "No":
        break