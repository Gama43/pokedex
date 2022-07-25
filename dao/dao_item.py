from dao.dao_abstract import DAO
from entidade.item import Item


class ItemDAO(DAO):
    def __init__(self):
        super().__init__('item.pkl')

    def add(self, item: Item):
        if (isinstance(item.nome, str) and (item is not None)) \
                and isinstance(item, Item):
            super().adicionar(item.nome, item)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        return super().remove(chave)