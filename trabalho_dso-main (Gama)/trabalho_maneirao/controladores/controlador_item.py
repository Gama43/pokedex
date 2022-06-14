from trabalho_maneirao.entidade.item import Item
from trabalho_maneirao.view import tela_item

class ControladorItem():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_itens = tela_item.TelaItem
        self.__itens = []

    @property
    def lista_itens(self) -> list:
        return  self.__itens 
        
    def incluir_item(self, nome : str, quantidade : int, raridade : int  ) -> Item:
        if isinstance(nome, str) and isinstance(quantidade, int) and \
            isinstance(raridade, int) and self.__itens is not None:

            self.__itens.append(tela_item.item_adicionar)
            return self.__itens 
    
    def excluir_item(self, nome : str, quantidade : int, raridade : int) -> Item:
        if isinstance(nome, str) and isinstance(quantidade, int) and \
            isinstance(raridade, int) and self.__itens is not None:

            self.__itens.remove(Item(nome, quantidade, raridade))
    

