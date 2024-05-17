list_og =[]
numbers = 0
method = ""
import funcionASC
import funcionDESC

while True:
    numbers = input("Ingrese los números por ordenar (END P/ FINALIZAR):  ")
    list_og.append(numbers)
    if numbers == "END":
        list_og.remove("END")
        method = input("Seleccione el método de orden (ASC/DESC):")
        if method == "ASC":
            list_od = funcionASC.ordenarA(list_og, "ASC")
            print("List Ordenada ASC:", list_od)
            break
        elif method == "DESC":
            list_od = funcionDESC.ordenarD(list_og, "DESC")
            print("Lista Ordenada DESC:", list_od)
            break
        else:
            print("Opción no valida. Intente de nuevo.") 
