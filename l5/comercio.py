from datetime import datetime,timedelta,date

class Comercio:
    def __init__(self,cliente:str, data:date):

        #Inicializando variaveis
        self.__cliente = ""
        self.__data = 0
        self.__itens = []
        
        #Chamando os setters
        self.cliente= cliente
        self.data = data

    #=== Getters e Setters ===
    @property
    def cliente (self) -> str:
        return self.__cliente
    
    @cliente.setter
    def cliente(self,cliente:str):
        if cliente == "":
            raise ValueError("Não é possivel cadastrar um carinho sem nome!")
        self.__cliente = cliente

    @property 
    def data(self) -> datetime:
        return self.__data
    
    @data.setter
    def data(self,data):
        self.__data = data

    #=== Metodos de Instancia ===

    def inserir(item:object):
        pass



class Item:
    #=== Construtor ===
    def __init__(self,prod:str,qtd:int,preco:float):

        #Inicializando variaveis
        self.__produto = ""
        self.__qtd = 0
        self.__preco_unit = 0.0

        #Chamando setters
        self.produto = prod
        self.qtd = qtd
        self.preco = preco

    #=== Getters e Setters ===
    @property
    def produto(self) ->str:
        return self.__produto
    
    @produto.setter
    def produto(self,prod:str):
        if prod == "":
            raise ValueError("Não é possivel cadastrar um produto sem nome!")
        self.__produto = prod


    @property
    def qtd(self) ->int:
        return self.__qtd
    
    @qtd.setter
    def qtd(self,qtd:str):
        if qtd <=0:
            raise ValueError("A quantidade deve ser maior que zero")
        
        elif qtd != int(qtd):
            raise ValueError("O valor deve ser inteiro!")
        self.__qtd = qtd


    @property
    def preco_unit(self) -> float:
        return self.__preco_unit
    
    @preco_unit.setter
    def preco_unit(self,preco:str):
        if preco <= 0:
            raise ValueError("O valor deve ser maior do que zero")
        self.__preco_unit = preco

    #=== Métodos da Instancia ===

    def total(self) -> float:
        return self.qtd * self.preco_unit
    
    def __str__(self):
        return f"Produto: {self.produto}, Quantidade: {self.qtd}, Valor Uni.: {self.preco_unit}, Total: {self.total()}"


        
        
    
