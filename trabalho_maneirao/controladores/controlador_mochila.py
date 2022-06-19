from trabalho_maneirao.entidade.mochila import Mochila
from trabalho_maneirao.view.tela_mochila import TelaMochila
from trabalho_maneirao.controladores.controlador_item import ControleItem


class ControladorMochila:

    def __init__(self, controlador_sistema):
        self.__tela_mochila = TelaMochila()
        self.__mochila = Mochila()
        self.__controle_item = ControleItem()
        self.__controlador_sistema = controlador_sistema

    def adicionar_item_na_mochila(self):
        self.__controle_item.lista_itens()
        self.__tela_mochila.seleciona_item()
        self.__mochila.mochila.append(self.__controle_item.itens)

    def excluir_item_da_mochila(self):
        pass

    def mostrar_itens_da_mochila(self):
        pass


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_item_na_mochila, 2: self.excluir_item_da_mochila, 3: self.mostrar_itens_da_mochila, 0: self.retornar()}


