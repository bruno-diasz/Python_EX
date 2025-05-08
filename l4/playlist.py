class PlayList:

    #=== Construtor ===
    def __init__(self, nome:str, desc:str):
        self.nome = nome
        self.descricao = desc
        self.musicas = []

    #=== Getters e Setters ===
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome:str):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self,desc:str):
        self.__descricao = desc
    
    #=== Metodos da instancia ===
    def __str__(self):
        return f'A playlist {self.nome} tem {len(self.musicas)} músicas'
    
    def inserir(self,musica):
        self.musicas.append(musica)
        
    def listar(self):
        return self.musicas

class Musica:
    def __init__(self, titulo:str, artista:str, album: str):
        self.titulo = titulo
        self.artista = artista
        self.album = album

    #=== Getters e Setters ===
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @property
    def artista(self):
        return self.__artista
    
    @artista.setter
    def artista(self, artista):
        self.__artista = artista

    @property
    def album(self):
        return self.__album
    
    @album.setter
    def album(self, album):
        self.__album = album

    #=== ToString ===
    def __str__(self):
        return f'Titulo: {self.titulo}\nArtista: {self.artista}\nAlbum: {self.album}\n'
    
newplay = None
while True:
    print("Digite um item do menu:")
    op = int(input("1- Criar playlist || 2- Inserir Musica || 3 - Listar músicas ||  0 - Sair\n"))
    if op == 1:
        nome = input("Digite o nome da playlist: ")
        desc = input("Digite a descrição da playlist: ")
        newplay = PlayList(nome,desc)
        print("Playlist Criada com sucesso!\n")

    elif op ==2:
        if  newplay == None:
            print("É necessario criar uma playlist para essa opção!!!\n")
            continue

        titulo = input("\nDigite o titulo da música : ")
        artista =input("Digite o nome do artista: ")
        album = input("Digite o album da música: ")
        musica = Musica(titulo, artista, album)
        newplay.inserir(musica)
        print("\nMúsica adicionada com sucesso!\n")

    elif op == 3:
        if  newplay == None:
            print("É necessario criar uma playlist para essa opção!!!\n")
            continue

        print("\n") 
        print(newplay)
        for musica in newplay.listar():
                print(musica)
        print("\n")


    elif op == 0:
        break

    else:
        print('Opção Invalida!\n')

    