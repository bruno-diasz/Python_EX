from cliente import Cliente
import json

class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj:object):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        for obj in cls.objetos:
            print(obj)

    @classmethod
    def listar_id(cls, id:int):
        for obj in cls.objetos:
            if obj.id == id:
                print(obj)

    @classmethod
    def atualizar(cls, obj):
        obj.nome = input("Digite o novo nome: ")
        obj.email = input("Digite o novo email: ")
        obj.fone = input("Digite o novo telefone: ")

    @classmethod
    def excluir(cls, obj):
        cls.objetos.remove(obj)

    @classmethod
    def salvar(cls):
        lista_clientes = []
        for obj in cls.objetos:
            lista_clientes.append(obj.to_dict())
        with open("l6/comercio_v2/clientes.json", mode="w") as arquivo:
            json.dump( lista_clientes , arquivo, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos = []    
        with open("l6/comercio_v2/clientes.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Cliente(obj["id"], obj["nome"], obj["email"],obj["fone"] )
                cls.objetos.append(c)



# x = Cliente(0,"Bruno","teste@email.com","123")
# y = Cliente(1,"Jorge","teste2@email.com","321")
# Clientes.inserir(x)
# Clientes.inserir(y)
# Clientes.salvar()

Clientes.abrir()
Clientes.abrir()
Clientes.listar()


