from clientes import Clientes, Cliente

class UI:
    @staticmethod
    def menu() -> int:
        print("\n#================ MENU =================#")
        print("Selecione o item que quer editar\n")
        print("1. Cliente | 2. Venda | 3. Sair\n")
        op = input("- Digite o número da opção desejada: ")

        if op == "1":
            print("\n#================= CLIENTE ==================#")
            print("Selecione uma das opções:\n")
            print("1. Listar clientes    | 2. Inserir clientes \n3. Atualizar clientes | 4. Excluir cliente\n")
            op += input("Digite o número da opção desejada: ")

        elif op == "2":
            print("\n#================= VENDA ==================#")
            print("Selecione uma das opções:\n")
            print("1. Listar vendas    | 2. Inserir vendas \n3. Atualizar vendas | 4. Excluir vendas\n")
            op += input("Digite o número da opção desejada: ")

        elif op =="3":
            return 3

        return int(op)
    
    @staticmethod
    def main():
        while True:
            op = UI.menu()
            if op == 11: UI.cliente_listar()
            elif op == 12: UI.cliente_inserir()
            elif op == 13: UI.cliente_atualizar()
            elif op == 14: UI.cliente_excluir()
            elif op == 3 : break
            else: print("Digite uma opção válida")

    
    @staticmethod
    def cliente_listar():
        print()
        try:
            clientes = Clientes.listar()
            for c in clientes:
                print(c)
        except:
            print("Você precisa ter pelo menos 1 cliente cadastrado")

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

UI.main()




