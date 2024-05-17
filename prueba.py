storage = {"solo": "alone"}
word_user= "start"

def exist(word):
    if word == "10":
        return 10
    if word in storage:
        return True
    else:
        return False

def read_storage():
    for word, trans in storage.items():
        word_user = input("Ingrese la palabra a traducir: ")
        if exist(word_user) == True:
            print(f"{word_user} significa {(storage [word_user])}")
        elif exist(word_user) == False:
            option = input("La palabra no esta registrada, ¿desea agregarla?: ")
            if option == "si":
                storage[word_user] = input("Ingrese la traduccion: ")
            elif option == "no":
                print("Entendido.")
            else:
                print("Opcion no valida.")
        elif exist(word_user) == 10:
            print("Cerrando programa.")
            break
read_storage()