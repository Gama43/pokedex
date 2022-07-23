from dao.dao_abstract import DAO
from entidade.treinador import Treinador


class AdminDAO(DAO):
    def __init__(self):
        super().__init__('admin.pkl')

    def add(self, treinador: Treinador):
        if (isinstance(treinador.nome, str) and (treinador is not None)) \
                and isinstance(treinador, Treinador):
            super().adicionar(treinador.nome, treinador)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        return super().remove(chave)
