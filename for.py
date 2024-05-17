
for x in range(5):
    if x == 0 or x==4:
        print("*"*5)
    else:
        print("*   *")

tablero = [
    ["h", "o", "l", "i", "s"],
    ["a", "l", "o", "o", "o"],
    ["h", "e", "l", "l", "o"],
    ["a", "e", "i", "o", "u"],
    ]
filas = 5
colum = 5
aciertos = 0
errores = 0

for f in range(filas):
    for c in range(colum):
        if ((f==0 or f==(filas-1)) or (c==0 or c==(colum-1)) ):
            print(tablero [f][c], end = "")
        else:
            print("  ")
    print(end="/n")
