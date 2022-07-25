
from controladores.controlador_admin import ControleTreinador
from controladores.controlador_pokemon import ControladorPokemon
from telas_gui.tela_relatorios import TelaRelatorios

class ControladorRelatorios():

    def __init__(self,controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__controlador_treinadores=ControleTreinador(self)
        self.__controlador_pokemon=ControladorPokemon(self)
        self.__tela_relatorio=TelaRelatorios()



    def abre_tela_relatorios(self):
        lista_opcoes = {1: self.listar_ordem_alfabetica,2:self.listar_nivel_crescente,3:self.listar_regiao,0: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_relatorio.tela_opcoes()]
            opcao_escolhida()


    def listar_ordem_alfabetica(self):
        lista_nomes = []
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_nomes.append(pokemon.nome)
        lista_nomes.sort()
        if len(lista_nomes)==0:
            self.__tela_relatorio.mostra_mensagem('Não foram registradas capturas de pokemon por esse treinador')
        else:
            self.__tela_relatorio.mostra_relatorio(lista_nomes)

    def listar_nivel_crescente(self):
        # self.__tela_pokemon.mostra_mensagem('-' * 40)
        # self.__tela_pokemon.mostra_mensagem('Lista de pokemons por ordem cresecente de nivel')
        # self.__tela_pokemon.mostra_mensagem('-' * 40)
        lista_levels=[]
        lista_printados=[]
        lista=[]
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_levels.append(pokemon.level)
        lista_levels.sort()
        if len(lista_levels)==0:
            self.__tela_relatorio.mostra_mensagem('Não foram registradas capturas de pokemon por esse treinador')

        else:
            i = 1
            for level in lista_levels:
                for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
                    if pokemon.level==level and pokemon not in lista_printados:
                        lista.append(f'Pokemon Nº{i}: {pokemon.nome}/ Nível: {pokemon.level}')
                        lista_printados.append(pokemon)
                        i+=1
            self.__tela_relatorio.mostra_relatorio(lista)



    def listar_regiao(self):

        regiao=self.__tela_relatorio.pega_regiao()
        lista_regioes=[]
        lista=[]
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_regioes.append(pokemon.regiao)
        lista.append(f'Pokemons da região: {regiao}')
        if regiao not in lista_regioes:
            self.__tela_relatorio.mostra_mensagem(f'Não foram cadastrados pokemons em {regiao}')
        else:
            c = 0
            for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
                if pokemon.regiao==regiao:
                    c+=1
                    lista.append('-' * 40)
                    lista.append(f'Pokemon Nº{c}: {pokemon.nome}')
            self.__tela_relatorio.mostra_relatorio(lista)



    def retornar(self):
        self.__controlador_sistema.tela()