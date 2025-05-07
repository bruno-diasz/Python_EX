class PlayList:

    #=== Construtor ===
    def __init__(self, nome:str, desc:str):
        self.nome = nome
        self.descricao = desc
        self.musicas = []

    #=== Getters e Setters ===
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome:str):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self,desc:str):
        self.__descricao = desc
