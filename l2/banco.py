class ContaBanco:
    def __init__(self):
       self.__nome_titular = "titular"
       self.__numero_conta = 0000
       self.__saldo = 0

    def sacar(self,saque):
        if self.__saldo >= saque:
            self.__saldo -= saque
        else:
            raise ValueError("Saldo insuficiente")
        
    def depositar(self, deposito):
        if deposito > 0.0:
            self.__saldo += deposito
        else:
            raise ValueError("Valor de deposito tem que ser positivo")
        
    @property
    def saldo(self):
        return self.__saldo
        

        
class UI:
    @staticmethod
    def menu():
        print("1-Sacar, 2-Depositar, 3-Ver Saldo, 9- Sair")
        return int(input())
    
    @staticmethod
    def main():
        usuario1 = ContaBanco()
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: usuario1.sacar(float(input("Digite um valor para saque: ").replace(",",".")))
            if op == 2: usuario1.depositar(float(input("Digite o valor para deposito: ").replace(",",".")))
            if op == 3: print(f"Seu saldo atual é de R$ {usuario1.saldo:.2f}".replace(",","."))


UI.main()