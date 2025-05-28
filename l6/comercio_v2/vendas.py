from venda import Venda
import json

class Vendas:
    objetos= []
    
    @classmethod
    def inserir(cls,obj:Venda):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls) -> list[Venda]:
        return cls.objetos

    @classmethod
    def listar_id(cls,id:int):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj:Venda):
        old_obj = cls.listar_id(obj.id)
        if x is not None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj:Venda):
        if x is not None:
            cls.objetos.remove(obj)
            cls.salvar()

    @classmethod
    def abrir(cls):
        with open("vendas.json", mode="r") as arquivo:
            vendas_json = json.load(arquivo)
            for obj in vendas_json:
                x = Venda(obj["id"])
                x.data, x.carrinho= obj["data"], obj["carrinho"]
                x.total,x.idCliente= obj["total"], obj["idCliente"]
                cls.objetos.append(x)

    @classmethod
    def salvar(cls)
        lista_vendas = []
        for obj in cls.objetos:
            lista_vendas.append(obj.to_dict())
        with open ("vendas.json", mode="w") as arquivo:
            json.dump(lista_vendas, arquivo, indent =4)




