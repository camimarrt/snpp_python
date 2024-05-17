def ordenarA(lista, orden):
    counter = 0
    for x in range(len(lista)-1):
        for y in range(len(lista)-1):
            if lista[y] >  (lista[y+1]):
                aux = lista[y]
                lista[y] = lista[y+1] 
                lista[y+1] = aux
            counter += 1
    print(f"Contador: {counter}")
    return lista
