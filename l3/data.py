class Data:
    def __init__(self, d:int, m:int, a:int):
        self.dia = d
        self.mes = m
        self.ano = a


    #=== Getters e Setters ===
    @property
    def dia(self) -> int:
        return self.__dia
    
    @dia.setter
    def dia(self,d :int):
        self.__dia= d
    
    @property
    def mes(self) -> int:
        return self.__mes
    
    @mes.setter
    def mes(self, m:int):
        if m >= 1 and m<= 12 and m == int(m):
            self.__mes=m
        else:
            raise ValueError("Mês Inválido!")
    
    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano (self,a:int):
        if a >=1 and a == int(a):
            self.__mes = a
        else:
            raise ValueError("Ano Inválido")

    @property
    def data(self) -> str:
        return self.__data
    
    @data.setter
    def data(self,d:str):
        self.dia,self.mes,self.ano = map(int, d.split('/'))
       
    #=== Metodos do Objeto ==

    def __str__(self):
        return f'A data {self.dia}/{self.mes}/{self.ano} é totalmente válida!'