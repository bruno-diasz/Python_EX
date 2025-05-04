from math import sqrt
class Equa2Grau:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    #=== Getters e setters===
    @property
    def a(self)-> float:
        return self.__a
    
    @a.setter
    def a(self, a :float):
        if a != 0 and a == float(a):
            self.__a = a
        else:
            raise ValueError("Valor não aceito")
    
    @property
    def b(self) -> float:
        return self.__b
    
    @b.setter
    def b (self,b:float):
        if b == float(b):
            self.__b = b
        else:
            raise ValueError("Valor não aceito")
        
    @property
    def c (self) -> float:
        return self.__c
    
    @c.setter
    def c(self,c:float):
        if c == float(c):
            self.__c = c
        else:
            raise ValueError("Valor não aceito")
    
    #=== Metodos do objeto ===

    def Delta(self) -> float :
        delta = self.b**2-4*self.a*self.c
        return delta
    
    def TemRaizesReais(self) -> bool:
        if self.Delta() >= 0:
            return True
        else:
            return False
    
    def Raiz1(self):
        x1 = (-self.b + sqrt(self.Delta()))/(2*self.a)
        return x1
    
    def Raiz2(self):
        x2 = (-self.b - sqrt(self.Delta()))/(2*self.a)
        return x2

    def __str__(self):
        return f'A = {self.a} || B = {self.b} || C = {self.c}'



