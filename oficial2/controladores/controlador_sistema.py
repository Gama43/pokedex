from oficial2.view.tela_sistema import TelaSistema
from oficial2.view.tela_login import TelaLogin
from oficial2.controladores.controlador_admin import ControleTreinador
from oficial2.view.tela_admin import TelaAdmin
from oficial2.view.tela_usuario import TelaUsuario
from oficial2.controladores.controlador_pokemon import ControladorPokemon
from oficial2.controladores.controlador_relatorios import ControladorRelatorios

class ControladorSistema:


    def __init__(self):
        self.__tela_sistema=TelaSistema()
        self.__tela_Login=TelaLogin()
        self.__tela_admin=TelaAdmin()
        self.__controlador_admin=ControleTreinador(self)
        self.__tela_usuario=TelaUsuario()
        self.__controlador_pokemon=ControladorPokemon(self)
        self.__controlador_relatorios=ControladorRelatorios(self)
        self.__usuario_logado=None


    @property
    def usuario_logado(self):
        return self.__usuario_logado


    def inicializa_sistema(self):
        self.abre_tela()


    def entrar(self):
        self.__usuario_logado=None
        situacao = False
        while situacao == False:
            dados_login = self.__tela_Login.tela_login()
            if dados_login["usuario"]=="admin":
                if dados_login["idpokedex"]=="admin":
                    self.__controlador_admin.abre_tela()
                    situacao=True
            else:
                self.__usuario_logado=self.__controlador_admin.valida_treinador(dados_login["usuario"],dados_login["idpokedex"])
                if not self.__usuario_logado:
                    print('Dados incorretos')
                else:
                    situacao = True
                    lista_opcoes = {1: self.gerenciar_pokemons, 2: self.relatorios,0:self.retornar}
                    while True:
                        opcao_escolhida = self.__tela_usuario.tela_opcoes()
                        funcao_escolhida = lista_opcoes[opcao_escolhida]
                        funcao_escolhida()
                        break




    def sair(self):
        self.__tela_admin.mostra_mensagem('Programa encerrado com sucesso, volte sempre!')
        exit(0)


    def abre_tela(self):
        lista_opcoes = {1: self.entrar, 2:self.sair}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()


    def retornar(self):
        self.entrar()

    def gerenciar_pokemons(self):
        self.__controlador_pokemon.abre_tela()

    def relatorios(self):
        self.__controlador_relatorios.abre_tela_relatorios()

    def tela(self):
        lista_opcoes = {1: self.gerenciar_pokemons, 2: self.relatorios, 0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_usuario.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
            break