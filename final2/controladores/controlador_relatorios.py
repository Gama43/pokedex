from final2.view.tela_usuario import TelaUsuario
from final2.view.tela_login import TelaLogin
from final2.view.tela_pokemon import TelaPokemon
from final2.controladores.controlador_admin import ControleTreinador
from final2.controladores.controlador_pokemon import ControladorPokemon
from final2.view.tela_relatorios import TelaRelatorio

class ControladorRelatorios():

    def __init__(self,controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__tela_pokemon=TelaPokemon()
        self.__tela_login=TelaLogin()
        self.__tela_usuario=TelaUsuario()
        self.__tela_relatorio=TelaRelatorio()
        self.__controlador_treinadores=ControleTreinador(self)
        self.__controlador_pokemon=ControladorPokemon(self)



    def abre_tela_relatorios(self):
        lista_opcoes = {1: self.listar_ordem_alfabetica,2:self.listar_nivel_crescente,3:self.listar_regiao,0: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_relatorio.tela_relatorios()]
            opcao_escolhida()


    def listar_ordem_alfabetica(self):
        self.__tela_pokemon.mostra_mensagem('-' * 40)
        lista_nomes = []
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_nomes.append(pokemon.nome)
        lista_nomes.sort()
        c = 1
        for nome in lista_nomes:
            self.__tela_pokemon.mostra_mensagem(f'Pokemon Nº{c}: {nome}')
            self.__tela_pokemon.mostra_mensagem('-' * 40)
            c+=1
        print('\n')
        if len(lista_nomes)==0:
            self.__tela_pokemon.mostra_mensagem('Não foram registradas capturas de pokemon por esse treinador')


    def listar_nivel_crescente(self):
        self.__tela_pokemon.mostra_mensagem('-' * 40)
        self.__tela_pokemon.mostra_mensagem('Lista de pokemons por ordem cresecente de nivel')
        self.__tela_pokemon.mostra_mensagem('-' * 40)
        lista_levels=[]
        lista_printados=[]
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_levels.append(pokemon.level)
        lista_levels.sort()
        i=1
        for level in lista_levels:
            for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
                if pokemon.level==level and pokemon not in lista_printados:
                    self.__tela_pokemon.mostra_mensagem(f'Pokemon Nº{i}: {pokemon.nome}/ Nível: {pokemon.level}')
                    self.__tela_pokemon.mostra_mensagem('-' * 40)
                    lista_printados.append(pokemon)
                    i+=1
        self.__tela_pokemon.mostra_mensagem('\n')
        if len(lista_levels)==0:
            self.__tela_pokemon.mostra_mensagem('Não foram registradas capturas de pokemon por esse treinador')


    def listar_regiao(self):
        print('-' * 40)
        regiao=self.__tela_pokemon.regiao()
        lista_regioes=[]
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_regioes.append(pokemon.regiao)
        self.__tela_pokemon.mostra_mensagem(f'Pokemons da região: {regiao}')
        c = 0
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            if pokemon.regiao==regiao:
                c+=1
                self.__tela_pokemon.mostra_mensagem('-' * 40)
                self.__tela_pokemon.mostra_mensagem(f'Pokemon Nº{c}: {pokemon.nome}')
        if regiao not in lista_regioes:
            self.__tela_pokemon.mostra_mensagem(f'Não foram cadastrados pokemons em {regiao}')


    def retornar(self):
        self.__controlador_sistema.tela()