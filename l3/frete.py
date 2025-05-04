class Frete:
    def __init__(self, d:float, p:float):
        self.peso = p
        self.distancia = d

    #=== Setter e getter para distancia ==
    @property
    def distancia(self) -> float:
        return self.__distancia
    
    @distancia.setter
    def distancia(self, d:float):
        if d > 0:
            self.__distancia = d
        else:
            raise ValueError("Valor deve ser positivo")
        
    #=== Setter e Getters para peso ===
    @property
    def peso(self) -> float:
        return self.__peso
    
    @peso.setter
    def peso(self,p:float):
        if p > 0:
            self.__peso = p
        else:
            raise ValueError("Valor do peso tem que ser positivo")
        
    #=== Metodos do objeto ===
    def __str__(self) -> str:
        return f'Distancia da viajem: {self.distancia}\nPeso da carga: {self.peso}'

    def CalcFrete(self) -> float:  
        valor = self.peso * self.distancia  / 100
        return valor
    
natal = Frete(100,2)
print(natal)
        