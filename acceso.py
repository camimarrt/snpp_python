errors = 0
user_info = {"michi": "miau"}

while errors < 3:
    user = input("Usuario:  ")
    if user in user_info:
        password = input("Contraseña:")
        if password in user_info[user]:
            print("Acceso Concedido.")
            break
        else: 
            errors += 1
            print("El usuario no existe. Intente de nuevo.")
    else:
        errors += 1
        print("El usuario no existe. Intente de nuevo.")
if errors == 3:
    print("Demasiados Intentos Fallidos.")
