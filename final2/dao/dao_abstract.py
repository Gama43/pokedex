import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))


    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def adicionar(self, chave, obj):
        self.__cache[chave] = obj
        self.__dump()

    def get(self, chave):
        try:
            return self.__cache[chave]
        except KeyError:
            pass

    def remove(self, chave):
        try:
            self.__cache.pop(chave)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()
