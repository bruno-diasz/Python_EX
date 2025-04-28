class Viagem:
    def __init__(self):
        self.__distancia= 0
        self.__tempo= 0
    
    # === Getter e Setter para distancia ===
    @property
    def distancia(self) -> float:
        return self.__distancia
    
    @distancia.setter
    def distancia(self, valor: float):
        if valor > 0: self.__distancia = valor
        else: raise ValueError("Digite um valor positivo")
    
    # === Getter e Setter para tempo ===
    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, valor:float):
        pass
        self.__tempo = valor
    
    # === Metódos da classe ===
    def velocidade_media(self) -> float:
        vm = self.__distancia/self.__tempo
        return vm

primeira_viajem = Viagem()
primeira_viajem.distancia=float(input("Digite a distancia: "))
primeira_viajem.tempo=float(input("Digite o tempo de viagem: "))
print(primeira_viajem.velocidade_media())
