from math import sqrt
class Retangulo:
    def __init__(self, b:int, h:int):
        self.b = b
        self.h = h
    #=== Getter e setter de B ===
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self,b: int):
        if b > 0:
            self.__b = b
        else:
            raise ValueError("Valor precisa ser positivo") 
        
     #=== Getter e setter de H ===
    @property
    def h(self):
        return self.__h
    @h.setter
    def h(self,h: int):
        if h > 0:
            self.__h = h
        else:
            raise ValueError("Valor precisa ser positivo") 
    
    #=== Metodos da Classe ===
    def CalcArea(self):
        return self.b*self.h
    
    def CalcDiagonal(self):
        return sqrt(self.b**2+self.h**2)
    
    def __str__(self):
        return f"Base = {self.b}\nAltura = {self.h}\nArea = {self.CalcArea()}\nDiagonal = {self.CalcDiagonal()}"
    
a= Retangulo(3,5)
print(a)