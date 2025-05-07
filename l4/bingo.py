import random
class Bingo:
    #=== Contrutor ===
    def __init__(self,numBolas:int):
        self.__numBolas = numBolas;
        self.__pote = list(range(1, numBolas + 1))
        random.shuffle(self.__pote)
        self.__bolas = []
    
    #=== Metodos da instancia ===
    def proximo(self) ->int:
        if not self.__pote:
            return -1
        bola = self.__pote.pop()
        self.__bolas.append(bola)
        return bola
    
    def sorteados(self) ->list:
        return self.__bolas


sorteio = Bingo(5)

while True:
    op = int(input("Digite um número: 1-Sortear 2-Lista dos sorteados 0-Sair"))
    if op == 1:
        print(sorteio.Proximo())
    elif op == 2:
        print(sorteio.Sorteados())
    elif op == 0:
        break;
    


