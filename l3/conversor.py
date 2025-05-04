class Conversor:
    def __init__(self,num:int):
        self.num = num

    #=== Setter e Getter de Num ===

    @property
    def num (self)-> int:
        return self.__num
    
    @num.setter
    def num(self,num:int):
        if not(isinstance(num, int)):
            raise ValueError("O valor não é inteiro")
        elif num<0:
            raise ValueError("O valor não é Positivo ou maior que zero")
        else:
            self.__num = num

    #=== Metodos do objeto ===
    def __str__(self)  -> str:
        return f'O Numero é: {self.num}'
    
    def Binario(self):
        n = self.num
        bin = []
        while n != 0:
            bin.insert(0,n%2)
            n = n//2
        return bin
    

#=== Main ===
n = int(input("Digite um numero inteiro positivo para começar: "))
x = Conversor(n)

while True:
    op = int(input("Escolha um item do menu:\n  1- Ver Numero atual || 2- Digitar novo numero || 3- Converter para binario || 0- Sair "))

    if op == 1:
        print(x)
    
    elif op == 2:
        n = int(input("Digite o novo numero: "))
        x.num = n

    elif op == 3:
        print(x.Binario())

    elif op == 0:
        break
