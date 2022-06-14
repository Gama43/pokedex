class Pokemon:

    def __init__(self,nome, tipo, level, ataques, defesa, regiao):
        self.__nome = nome
        self.__tipo = tipo
        self.__level = level
        self.__ataques = ataques
        self.__defesa = defesa
        self.__regiao = regiao


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__treinador = level

    @property
    def ataques(self):
        return self.__ataques

    @ataques.setter
    def ataques(self, ataques):
        self.__ataques = ataques

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, defesa):
        self.__defesa = defesa

    @property
    def regiao(self):
        return self.__regiao

    @regiao.setter
    def regiao(self, regiao):
        self.__regiao = regiao