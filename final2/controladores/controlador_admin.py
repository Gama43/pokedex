
from final2.entidade.treinador import Treinador
from final2.controladores.controlador_item import ControleItem
from final2.telas_gui.tela_admin import TelaAdmin
from final2.telas_gui.tela_pokemon import TelaPokemon
from final2.dao.dao_admin import AdminDAO


class ControleTreinador:

    def __init__(self, controlador_sistema):
        self.__treinadores = []
        self.__tela_treinador = TelaAdmin()
        self.__tela_pokemon=TelaPokemon()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_item=ControleItem(self)
        self.__tela_admin=TelaAdmin()
        self.__admin_dao=AdminDAO()


    @property
    def treinadores(self):
        return self.__admin_dao.get_all()


    def pega_treinador_por_idpokedex(self, idpokedex: int):
        for treinador in self.__admin_dao.get_all():
            if (treinador.idpokedex == idpokedex):
                return treinador
        return None


    def adicionar_treinador(self):
        dados_treinador=self.__tela_treinador.dados_treinador()
        if dados_treinador=='voltar':
            self.abre_tela()
        nome=dados_treinador["nome"]
        idpokedex=dados_treinador["idpokedex"]

        if nome and idpokedex:
            cont=0
            for treinador in self.treinadores:
                if treinador.idpokedex==idpokedex:
                    cont+=1
            if cont==0:
                treinador=Treinador(nome,idpokedex)
                self.__admin_dao.add(treinador)
            else:
                self.__tela_admin.mostra_mensagem('ERRO! Esse idpokedex ja foi cadastrado.')
        else:
            self.__tela_treinador.mostra_mensagem('Por favor, deixa de ser burro')

    def lista_treinadores(self):
        sit = True
        dados_treinadores = []
        for treinador in self.__admin_dao.get_all():
            dados_treinadores.append({"nome": treinador.nome, "idpokedex": treinador.idpokedex})
            sit = False

        if sit:
            self.__tela_pokemon.mostra_mensagem('Não foram registrados treinadores no sistema')
        else:
            self.__tela_treinador.mostra_treinador(dados_treinadores)

    def alterar_treinador(self):
        idpokedex = self.__tela_treinador.id_treinador()
        if idpokedex=='voltar':
            self.abre_tela()
        treinador = self.pega_treinador_por_idpokedex(idpokedex)

        if (treinador is not None):
            novos_dados_treinador = self.__tela_treinador.dados_treinador()
            treinador.nome = novos_dados_treinador["nome"]
            treinador.idpokedex = novos_dados_treinador["idpokedex"]
        else:
            self.__tela_treinador.mostra_mensagem("ATENCAO! Esse treinador não existe")


    def excluir_treinador(self):
        if len(self.__treinadores)>0:
            idpokedex = self.__tela_treinador.id_treinador()
            if idpokedex == 'voltar':
                self.abre_tela()
            treiandor= self.pega_treinador_por_idpokedex(idpokedex)
            if (treiandor is not None):
                self.__admin_dao.remove(treiandor)
            else:
                self.__tela_treinador.mostra_mensagem("ATENCAO! Esse treinador não existe")
        else:
            self.__tela_admin.mostra_mensagem('Ainda não foram registrados treinadpres nesse sistema')


    def valida_treinador(self,nome,idpokedex):
        for treinador in self.__treinadores:
            if treinador.nome==nome and treinador.idpokedex==str(idpokedex):
                return treinador

    def ver_todos_pokemons(self):
        sit=True
        lista=[]
        for treinador in self.__treinadores:
            for pokemon in treinador.lista_pokemons:
                lista.append({"nome": treinador.nome,'pokemon':pokemon.nome ,"level": pokemon.level})
                sit = False
        if sit==False:
            self.__tela_treinador.todos_pokemons(lista)
        if sit:
            self.__tela_admin.mostra_mensagem('Não foram registrados capturas de pokemon no sistema')

    def ver_pokemon_por_nome(self):
        nome=self.__tela_pokemon.nome_pokemon()
        sit=False
        lista=[]
        for treinador in self.__treinadores:
            for pokemon in treinador.lista_pokemons:
                if pokemon.nome==nome:
                    sit=True
                    lista.append({"nome": treinador.nome,'pokemon':pokemon.nome ,"level": pokemon.level})
                    break
        if sit:
            self.__tela_treinador.pokemon_por_nome(lista)
        if sit==False:
            texto='Não foram registrados capturas desse pokemon'
            self.__tela_admin.mostra_mensagem(texto)


    def gerenciar_itens(self):
        self.__controlador_item.abre_tela()


    def retornar(self):
        self.__controlador_sistema.entrar()


    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_treinador, 3: self.alterar_treinador, 2: self.excluir_treinador, 4: self.lista_treinadores,
                         0: self.retornar,5: self.ver_todos_pokemons,7:self.ver_pokemon_por_nome,6:self.gerenciar_itens}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_admin.tela_opcoes()]
            opcao_escolhida()
