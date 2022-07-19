

class Pokemon:

    def __init__(self,nome, tipo, level, nomeataque1,valorataque1,nomeataque2,valorataque2, defesa, regiao):
        self.__nome = nome
        self.__tipo = tipo
        self.__level = level
        self.__nomeataque1 = nomeataque1
        self.__valorataque1=valorataque1
        self.__nomeataque2 = nomeataque2
        self.__valorataque2=valorataque2

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
        self.__level= level

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

    @property
    def nomeataque1(self):
        return self.__nomeataque1

    @nomeataque1.setter
    def nomeataque1(self, nomeataque1):
        self.__nomeataque1 = nomeataque1

    @property
    def nomeataque2(self):
        return self.__nomeataque2

    @nomeataque2.setter
    def nomeataque2(self, nomeataque2):
        self.__nomeataque2 = nomeataque2

    @property
    def valorataque2(self):
        return self.__valorataque2

    @valorataque2.setter
    def valorataque2(self, valorataque2):
        self.__valorataque2 = valorataque2

