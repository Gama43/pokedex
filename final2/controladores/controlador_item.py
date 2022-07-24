from final2.entidade.item import Item
from final2.telas_gui.tela_item import TelaItem
from final2.dao.dao_item import ItemDAO


class ControleItem:

    def __init__(self, controlador_sistema):
        self.__item_dao = ItemDAO()
        self.__tela_item = TelaItem()
        self.__controlador_sistema = controlador_sistema

    @property
    def itens(self):
        return self.__item_dao.get_all()

    def pega_item_por_nome(self, nome: str):
        for item in self.__item_dao.get_all():
            if item.nome == nome:
                return item
        return None

    def adicionar_item(self):
        dados_item = self.__tela_item.dados_item()
        if dados_item == 'voltar':
            self.abre_tela()
        nome = dados_item["nome"]
        quantidade = dados_item["quantidade"]
        raridade = dados_item["raridade"]
        cont = 0
        for item in self.itens:
            if item.nome == nome:
                cont += 1
        if cont == 0:
            item = Item(nome, quantidade, raridade)
            self.__item_dao.add(item)
        else:
            self.__tela_item.mostra_mensagem('Item já existe')

    def lista_itens(self):
        sit = True
        dados_item = []
        for item in self.__item_dao.get_all():
            dados_item.append({"nome": item.nome, "quantidade": item.quantidade, "raridade": item.raridade})
            sit = False

        if sit:
            self.__tela_item.mostra_mensagem('Não foram registrados itens no sistema')
        else:
            self.__tela_item.mostra_item(dados_item)

    def alterar_item(self):
        nome = self.__tela_item.nome_item()
        if nome == 'voltar':
            self.abre_tela()
        item = self.pega_item_por_nome(nome)

        if item is not None:
            novos_dados_item = self.__tela_item.dados_item()
            item.nome = novos_dados_item["nome"]
            item.quantidade = novos_dados_item["quantidade"]
            item.raridade = novos_dados_item["raridade"]
            self.lista_itens()
        else:
            self.__tela_item.mostra_mensagem("ITEM NÃO CADASTRADO")

    def excluir_item(self):
        nome = self.__tela_item.nome_item()
        if nome == 'voltar':
            self.abre_tela()
        item = self.pega_item_por_nome(nome)
        if item is not None:
            self.__item_dao.remove(item)
        else:
            self.__tela_item.mostra_mensagem("ATENCAO! Esse Item não existe")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_item, 2: self.alterar_item, 3: self.excluir_item, 4: self.lista_itens,
                        0: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_item.tela_opcoes()]
            opcao_escolhida()