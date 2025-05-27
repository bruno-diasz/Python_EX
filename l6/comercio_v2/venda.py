from datetime import date
class Venda:
    def __init__(self,id:int):
        self.id = id #Chamando setter

        self.__data = None
        self.__carrinho = None
        self.__total = 0
        self.__idCliente = 0

    #Getters e setters
    @property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O valor o id deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O id deve ser maior ou igual a zero")
        self.__id= valor

    @property
    def data(self) -> date:
        return self.__data 
    @data.setter
    def data(self,valor:date):
        if not isinstance(valor, date):
            raise TypeError("O valor da data deve ser um do tipo date")
        self.__data = valor

    @property
    def carrinho(self) -> int:
        return self.__carrinho
    @carrinho.setter
    def carrinho(self,valor:int):
        if not isinstance(valor, bool):
            raise TypeError("O valor o carrinho deve ser um verdadeiro ou falso")
        self.__carrinho= valor

    @property
    def total(self) ->float:
        return self.__total
    @total.setter
    def total(self, valor:float):
        if not isinstance(valor, (float,int)):
            raise TypeError("O valor o total deve ser um número")
        if valor < 0:
            raise ValueError("O valor deve ser maior ou igual a zero")
        self.__total= valor

    @property
    def idCliente(self) -> int:
        return self.__idCliente
    @idCliente.setter
    def idCliente(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O valor o idCliente deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O idCliente deve ser maior ou igual a zero")
        self.__idCliente= valor

    #Metodos de instancia
    def __str__(self):
        return f"{self.id}. {self.data} - carrinho:{self.carrinho} - R$ {self.total:.2f}. idCliente:{self.idCliente}"
    



    