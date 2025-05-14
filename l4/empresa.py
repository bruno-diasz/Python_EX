class Empresa:

    #===Metodo construtor ===
    def __init__(self, nome:str):
        self.__nome = None
        self.__clientes = []

        self.nome = nome
    
    #=== Getters e Setters ===
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self,nome):
        if nome == "": raise ValueError("O Nome nao pode ser vazio")
        self.__nome = nome

    @property
    def clientes(self):
        return self.__clientes
    
    

    #=== Metodos de Instância ===
    def inserir(self, cliente:object):
        self.clientes.append(cliente)

    def listar(self):
        return self.clientes

class Cliente:
    #=== Metodos construtor ===
    def __init__(self,nome:str, cpf:str, limite:float):
        self.__nome = None      #Inicializando atributos
        self.__cpf = None       #Inicializando atributos
        self.__limite = 0.0     #Inicializando atributos
        self.__socio = None     #Inicializando atributos

        self.nome = nome        # chama o setter
        self.cpf = cpf          # chama o setter
        self.limite = limite    # chama o setter
       
    
    #=== Getters e Setters ===
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str):
        if nome == "": raise ValueError("O Nome nao pode ser vazio")
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf:str):
        self.__cpf = cpf
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite:float):
        if limite < 0: raise ValueError("Valor solicitado invalido")
        self.__limite = limite
    
    @property
    def socio(self):
        return self.__socio
    
    @socio.setter
    def socio(self, cliente:object):
        if self.__socio != None:
            self.__socio.__socio = None
        self.__socio = cliente
        if cliente.__socio != None:
            cliente.__socio.__socio = None
        cliente.__socio = self

    #=== Metodo ToStrig === 
    def __str__(self):
        imprimir = ""
        if self.socio == None:
            imprimir = f"\nNome: {self.nome}\nCPF: {self.cpf}\nLimite: {self.limite}\n"
        else:
            imprimir = f"\nNome: {self.nome}\nCPF: {self.cpf}\nLimite: {self.limite}\nSocio: {self.socio.nome}\n"

        return imprimir
    
class UI:
    @staticmethod
    def menu():
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Criar empresa")
        print("2 - Cadastrar cliente")
        print("3 - Listar clientes")
        print("4 - Associar clientes")
        print("9 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            return 0

    @staticmethod
    def main():
        empresa = None

        while True:
            op = UI.menu()

            if op == 1:
                empresa = UI.criar_empresa()
                print(f"✅ Empresa '{empresa.nome}' criada com sucesso!")

            elif op == 2:
                if empresa is None:
                    print("⚠️ Crie uma empresa primeiro!")
                    continue
                UI.cadastrar_cliente(empresa)
                print("✅ Cliente cadastrado com sucesso!")

            elif op == 3:
                if empresa is None:
                    print("⚠️ Crie uma empresa primeiro!")
                    continue
                print("\n📋 Lista de Clientes:")
                UI.lista_clientes(empresa)

            elif op == 4:
                if empresa is None:
                    print("⚠️ Crie uma empresa primeiro!")
                    continue
                print("\n🔗 Associação de Clientes:")
                UI.associar_cliente(empresa)

            elif op == 9:
                print("👋 Encerrando o programa. Até logo!")
                break

            else:
                print("❌ Opção inválida. Tente novamente.")

    @staticmethod
    def criar_empresa():
        nome = input("Informe o nome da nova empresa: ")
        return Empresa(nome)

    @staticmethod
    def cadastrar_cliente(empresa: Empresa):
        print("\n📌 Cadastro de Cliente:")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        try:
            limite = float(input("Limite de crédito: "))
            cliente = Cliente(nome, cpf, limite)
            empresa.inserir(cliente)
        except ValueError:
            print("❌ Limite inválido. Operação cancelada.")

    @staticmethod
    def lista_clientes(empresa: Empresa):
        clientes = empresa.listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
            return
        for i, cliente in enumerate(clientes):
            print(f"\nCliente {i}:")
            print(cliente)

    @staticmethod
    def associar_cliente(empresa: Empresa):
        clientes = empresa.listar()
        if len(clientes) < 2:
            print("⚠️ É necessário pelo menos dois clientes para associar.")
            return

        print("Clientes disponíveis:")
        for i, cliente in enumerate(clientes):
            print(f"{i} - {cliente.nome} (CPF: {cliente.cpf})")

        try:
            idx1 = int(input("Digite o índice do primeiro cliente: "))
            idx2 = int(input("Digite o índice do segundo cliente: "))

            if idx1 == idx2:
                print("❌ Não é possível associar um cliente a ele mesmo.")
                return

            cliente1 = clientes[idx1]
            cliente2 = clientes[idx2]

            cliente1.socio = cliente2
            print(f"✅ {cliente1.nome} agora está associado a {cliente2.nome}.")

        except (ValueError, IndexError):
            print("❌ Índice inválido. Operação cancelada.")

UI.main()