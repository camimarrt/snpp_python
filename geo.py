class   Rectangle:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def perimetro(self):
        return 2*(self.largo +self.ancho)
    
    def area(self):
        return (self.largo*self.ancho)
    
class Square:
    def __init__(self, lado):
        self.lado = lado
        super().__init__(lado, lado)
        
if __name__ == "__main__":
    rectangulo = Rectangle(4,2)
    print(f"El área del rectangulo es: {rectangulo.area()}")
