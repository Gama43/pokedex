from trabalho_maneirao.view.tela_usuario import TelaUsuario
from trabalho_maneirao.view.tela_login import TelaLogin
from trabalho_maneirao.view.tela_pokemon import TelaPokemon
from trabalho_maneirao.entidade.pokemon import Pokemon
from trabalho_maneirao.entidade.treinador import Treinador
from trabalho_maneirao.controladores.controlador_admin import ControleTreinador



class ControladorUsuario():

    def __init__(self,controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__tela_pokemon=TelaPokemon()
        self.__tela_login=TelaLogin()
        self.__tela_usuario=TelaUsuario()
        self.__controlador_treinadores=ControleTreinador(self)


    def treinador(self,nome,idpokedex):
        self.__treinador=Treinador(nome,idpokedex)
        return self.__treinador


    def capturar_pokemon(self):
        print(self.treinador(self,self))
        dados_pokemon = self.__tela_pokemon.dados_pokemon()
        nome = dados_pokemon["nome"]
        tipo = dados_pokemon["tipo"]
        level = dados_pokemon["level"]
        ataques = dados_pokemon["ataques"]
        defesa = dados_pokemon["defesa"]
        regiao = dados_pokemon["regiao"]
        pokemon = Pokemon(nome, tipo, level, ataques, defesa, regiao)

        self.__treinador.lista_pokemons.append(pokemon)


    def lista_pokemons(self):

        for pokemon in self.__treinador.lista_pokemons:
            self.__tela_pokemon.mostra_pokemon({"nome": pokemon.nome, "tipo": pokemon.tipo,"level": pokemon.level, "ataques": pokemon.ataques, "defesa": pokemon.defesa, "regiao": pokemon.regiao})

    def alterar_pokemon(self):
        pass

    def excluir_pokemon(self):
        pass

    def evoluir_pokemon(self):
        pass

    def transferir_pokemon(self):
        pass

    def ver_mochila(self):
        pass

    def retornar(self):
        self.__controlador_sistema.entrar()

    def abre_tela(self):
        lista_opcoes = {1: self.capturar_pokemon, 2: self.lista_pokemons,0: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_usuario.tela_usuario()]
            opcao_escolhida()



