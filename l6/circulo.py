import math

class Circulo:
    def __init__(self):
        self.__raio = 0
        

    #=== Getter e Setter ===
    @property
    def raio(self) -> float:
        return self.__raio
    
    @raio.setter
    def raio(self,valor: int):
        if valor >= 0: self.__raio = valor
        else: raise ValueError("O valor deve ser positivo")

    #=== Metodos da classe ===
    def calc_area(self) -> float:
        area = math.pi * self.__raio ** 2
        return area  
    
    def calc_circunferencia(self) -> float:
        circunferencia = 2 * math.pi * self.__raio 
        return circunferencia
    
    def __str__(self):
        return f'Seu raio é: {self.__raio}'



