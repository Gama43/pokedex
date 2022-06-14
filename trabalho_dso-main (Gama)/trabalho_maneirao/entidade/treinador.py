class Treinador:

    def __init__(self, nome: str, idpokedex: int):
        self.__nome = nome
        self.__idpokedex = idpokedex
        self.__lista_pokemons=[]

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def idpokedex(self):
        return self.__idpokedex

    @idpokedex.setter
    def idpokedex(self, idpokedex):
        self.__idpokedex = idpokedex

    @property
    def lista_pokemons(self):
        return self.__lista_pokemons
