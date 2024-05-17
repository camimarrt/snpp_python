kilometro = float(input("Ingrese la Distancia Recorrida:"))
comb = float(input("Ingrese el combustible comsumido:"))
comb_kilo = (kilometro/comb)**-1
print("El consumo de combustible por kilometro fue de:" , "{:.3f}".format(comb_kilo))
