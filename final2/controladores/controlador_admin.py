from final2.view.tela_admin import TelaAdmin
from final2.entidade.treinador import Treinador
from final2.view.tela_pokemon import TelaPokemon
from final2.controladores.controlador_item import ControleItem
from final2.telas_gui.tela_admin import TelaAdmin

class ControleTreinador:

    def __init__(self, controlador_sistema):
        self.__treinadores = []
        self.__tela_treinador = TelaAdmin()
        self.__tela_pokemon=TelaPokemon()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_item=ControleItem(self)
        self.__tela_admin=TelaAdmin()


    @property
    def treinadores(self):
        return self.__treinadores


    def pega_treinador_por_idpokedex(self, idpokedex: int):
        for treinador in self.__treinadores:
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
                self.__treinadores.append(treinador)
            else:
                self.__tela_pokemon.mostra_mensagem('ERRO!')
        else:
            self.__tela_treinador.mostra_mensagem('Por favor, deixa de ser burro')

    def lista_treinadores(self):
        sit = True
        dados_treinadores = []
        for treinador in self.__treinadores:
            dados_treinadores.append({"nome": treinador.nome, "idpokedex": treinador.idpokedex})
            sit = False
        self.__tela_treinador.mostra_treinador(dados_treinadores)
        if sit:
            self.__tela_pokemon.mostra_mensagem('Não foram registrados treinadores no sistema')

    def alterar_treinador(self):
        idpokedex = self.__tela_treinador.id_treinador()
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
            treiandor= self.pega_treinador_por_idpokedex(idpokedex)
            if (treiandor is not None):
                self.__treinadores.remove(treiandor)
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
        for treinador in self.__treinadores:
            for pokemon in treinador.lista_pokemons:
                self.__tela_admin.mostra_mensagem("-"*40)
                self.__tela_admin.mostra_mensagem(f'Treinador: {treinador.nome}: {pokemon.nome} ,nível {pokemon.level}')
                sit = False
        if sit == True:
            self.__tela_admin.mostra_mensagem('Não foram registrados capturas de pokemon no sistema')

    def ver_pokemon_por_nome(self):
        nome=self.__tela_pokemon.nome()
        sit=False
        for treinador in self.__treinadores:
            for pokemon in treinador.lista_pokemons:
                if pokemon.nome==nome:
                    sit=True
                    self.__tela_pokemon.mostra_mensagem("-" * 30)
                    texto=(f'Treinador: {treinador.nome}:{pokemon.nome} ,nível {pokemon.level}')
                    self.__tela_pokemon.mostra_mensagem(texto)
                    break
        if sit==False:
            texto='Não foram registrados capturas desse pokemon'
            self.__tela_pokemon.mostra_mensagem(texto)


    def gerenciar_itens(self):
        self.__controlador_item.abre_tela()


    def retornar(self):
        self.__controlador_sistema.entrar()


    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_treinador, 3: self.alterar_treinador, 2: self.excluir_treinador, 4: self.lista_treinadores,
                         0: self.retornar,5: self.ver_todos_pokemons,6:self.ver_pokemon_por_nome,7:self.gerenciar_itens}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_admin.tela_opcoes()]
            opcao_escolhida()