class Item:

    def __init__(self, nome, quantidade, raridade):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__raridade = raridade

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def raridade(self):
        return self.raridade
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @quantidade.setter
    def nome(self, quantidade):
        self.__quantidade = quantidade
    
    @raridade.setter
    def raridade(self, raridade):
        self.__raridade = raridade
