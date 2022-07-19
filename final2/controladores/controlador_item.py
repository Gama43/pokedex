from final2.view.tela_item import TelaItem
from final2.entidade.item import Item


class ControleItem:

    def __init__(self, controlador_sistema):
        self.__itens = []
        self.__tela_item = TelaItem()
        self.__controlador_sistema = controlador_sistema


    @property
    def itens(self):
        return self.__itens

    def pega_item_por_nome(self, nome: str):
        for item in self.__itens:
            if item.nome == nome:
                return item
        return None

    def adicionar_item(self):
        dados_item = self.__tela_item.dados_item()
        nome = dados_item["nome"]
        quantidade = dados_item["quantidade"]
        raridade = dados_item["raridade"]
        cont = 0
        for item in self.itens:
            if item.nome == nome:
                cont += 1
        if cont == 0:
            item = Item(nome, quantidade,raridade)
            self.__itens.append(item)
        else:
            print('ERRO!')

    def lista_itens(self):
        n_itens = 1
        for item in self.__itens:
            print(f"Opção: {n_itens} \n")
            self.__tela_item.mostra_item({"nome": item.nome, "quantidade": item.quantidade, "raridade": item.raridade})

            n_itens += 1

    def alterar_item(self):
        self.lista_itens()
        nome = self.__tela_item.seleciona_item()
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
        self.lista_itens()
        nome = self.__tela_item.seleciona_item()
        item = self.pega_item_por_nome(nome)

        if item is not None:
            self.__itens.remove(item)
            self.lista_itens()
        else:
            self.__tela_item.mostra_mensagem("ITEM NÃO CADASTRADO")


    def retornar(self):
        self.__controlador_sistema.abre_tela()


    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_item, 2: self.alterar_item, 3: self.excluir_item, 4: self.lista_itens, 0:self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_item.tela_opcoes()]
            opcao_escolhida()