import math

class Circulo:
    def __init__(self):
        self.__raio = 0
        self.__altura = 0

    @property
    def raio(self) -> float:
        return self.__raio
    @raio.setter
    def raio(self,valor: int):
        if valor > 0: self.__raio = valor
        else: raise ValueError("O valor deve ser positivo")
        
    
    def calc_area(self) -> float:
        area = math.pi * self.__raio ** 2
        return area  
    def calc_circunferencia(self):
        circunferencia = 2 * math.pi * self.__raio 
        return circunferencia

circulo= Circulo()
circulo.raio = int(input("digite um numero: "))
print(circulo.raio)
print (circulo.calc_area())


