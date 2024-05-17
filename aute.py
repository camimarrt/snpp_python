class Auto:
    def __init__(self, modelo, marca, color,):
        self.modelo = modelo
        self.marca= marca
        self.color = color
        self.estado = ""
        self.motor = Motor(cilindros=4)
    def acelerar(self,tipo=""):
        if tipo == "Despacio":
            self.motor.inyectar_gasolina(10)
        else:
            self.motor.inyectar_gasolina(40)

        self.estado = "en_movimiento."
    def info(self):
        return f"Modelo: {self.modelo}. Marca: {self.marca}. Color: {self.color}. Estado: {self.estado}."
class Motor:
    def __init__(self, cilindros, tipo = "Diesel"):
       self.cilindros = cilindros
       self.tipo = tipo
       self.temperatura = 0

    def inyectar(self, litros = 0):
        pass
    def info(self):
        return f"Cantidad de Cilindros {self.cilindros}, tipo{self.tipo}."
    
if __name__ == "__main__":
    mi_motor = Motor(8, "Diesel")

    mi_auto =Auto("Tundra", "Toyota","Azul")
    mi_auto.motor = mi_motor
    print(mi_auto.info())
    print(mi_auto.motor.info())