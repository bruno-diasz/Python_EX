from dao.clientes import Clientes, Cliente
from dao.produtos import Produtos, Produto
from dao.vendas import Vendas, Venda

class UI:
    carrinho = None

    @staticmethod
    def menu() -> int:
        print("\n#================ LOGIN =================#")
        print("Selecione o tipo de login: ")
        usr = input("1. Admin | 2. Cliente ")
            
        if usr == "1":
            print("\n#================ MENU ADMIN =================#")
            print("Selecione o item que quer editar\n")
            print("1. Cliente | 2. Produto | 9. Sair\n")
            op = usr+input("- Digite o número da opção desejada: ")

            if op == "11":
                print("\n#================= CLIENTE ==================#")
                print("Selecione uma das opções:\n")
                print("1. Listar    | 2. Inserir\n3. Atualizar | 4. Excluir\n")
                op += input("Digite o número da opção desejada: ")

            elif op == "12":
                print("\n#================= PRODUTO ==================#")
                print("Selecione uma das opções:\n")
                print("1. Listar    | 2. Inserir\n3. Atualizar | 4. Excluir\n")
                op += input("Digite o número da opção desejada: ")

            elif op =="19":
                return 3

            return int(op)
        
        elif usr == "2":
            print("\n#================ MENU CLIENTE =================#")
            print("Selecione o item que quer editar\n")
            print("1. Iniciar carrinho de compras | 2. Listar as compras | 3. inserir produto no carrinho\n")
            op = usr+input("- Digite o número da opção desejada: ")

            return int(op)
        
    @staticmethod
    def main():
        while True:
            op = UI.menu()
            if op == 111: UI.cliente_listar()
            elif op == 112: UI.cliente_inserir()
            elif op == 113: UI.cliente_atualizar()
            elif op == 114: UI.cliente_excluir()

            elif op == 121: UI.produto_listar()
            elif op == 122: UI.produto_inserir()
            elif op == 123: UI.produto_atualizar()
            elif op == 124: UI.produto_excluir()

            elif op == 21: UI.venda_iniciar()
            elif op == 22: UI.venda_listar()
            elif op == 23: UI.venda_inserir_item()

            elif op == 3 : break
            else: print("Digite uma opção válida", op)

    #======CRUD Cliente======
    @staticmethod
    def cliente_listar():
        print()
        clientes = Clientes.listar()
        for c in clientes:
            print(c)
        
    @staticmethod
    def cliente_inserir():
        nome = input("Digite o nome do cliente:")
        email = input("Digite o email do cliente:")
        fone = input("Digite o telefone do cliente:")
        x = Cliente(0,nome,email,fone)
        Clientes.inserir(x)

    @staticmethod
    def cliente_atualizar():
        id = int(input("Digite o ID o cliente que deseja atualizar: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")        
        x = Cliente(id, nome, email, fone)
        Clientes.atualizar(x)

    @staticmethod
    def cliente_excluir():
        id = int(input("Digite o ID o cliente que deseja excluir: "))
        x = Clientes.listar_id(id)
        Clientes.excluir(x)

    #====== CRUD Produto======

    @staticmethod
    def produto_listar():
        print()
        produtos = Produtos.listar()
        for c in produtos:
            print(c)
        

    @staticmethod
    def produto_inserir():
        desc = input("Digite a descrição do produto:")
        preco = float(input("Digite o preço do produto:"))
        estoq = int(input("Digite a quantidade em estoque:"))
        x = Produto(0,desc,preco,estoq)
        Produtos.inserir(x)

    @staticmethod
    def produto_atualizar():
        id = int(input("Digite o ID do produto que deseja atualizar: "))
        desc = input("Digite a nova descrição:")
        preco = float(input("Digite o novo preço: "))
        estoq = int(input("Digite a quantidade em estoque atualizada:"))
        x = Produto(id,desc,preco,estoq)
        Produtos.atualizar(x)

    @staticmethod
    def produto_excluir():
        id = int(input("Digite o ID o produto que deseja excluir: "))
        x = Produtos.listar_id(id)
        Produtos.excluir(x)

    #Venda
    @classmethod
    def venda_iniciar(cls):
        x =  Venda(0)
        Vendas.inserir(x)
        cls.carrinho = x
        
    def venda_inserir_item():
        pass

    def venda_listar():
        for v in Vendas.listar():
            print(v)

    def venda_confirmar():
        pass
UI.main()




