class Calculadora:
    num1 = None
    num2 = None

    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def set_numeros(self,x,y):
        self.num1 = x 
        self.num2 = y 

    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    def mul(self):
        return (self.num1*self.num2) 
    def div(self):
        return (self.num1/self.num2) 
    def pot(self):
        return (self.num1**self.num2)

