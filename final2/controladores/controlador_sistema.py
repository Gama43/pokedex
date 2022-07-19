from final2.view.tela_sistema import TelaSistema
from final2.telas_gui.tela_login import TelaLogin
from final2.controladores.controlador_admin import ControleTreinador
from final2.view.tela_admin import TelaAdmin
from final2.view.tela_usuario import TelaUsuario
from final2.controladores.controlador_pokemon import ControladorPokemon
from final2.controladores.controlador_relatorios import ControladorRelatorios
from final2.telas_gui.tela_pokemon import TelaPokemon
from final2.telas_gui.tela_usuario import TelaUsuario

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
        self.__tela_usuario=TelaUsuario()
        self.__tela_pokemon=TelaPokemon()


    @property
    def usuario_logado(self):
        return self.__usuario_logado


    def inicializa_sistema(self):
        self.entrar()


    def entrar(self):
        self.__usuario_logado=None
        situacao = False
        while situacao == False:
            cadastro = self.__tela_Login.dados_login()
            if cadastro:
                if cadastro["usuario"]=="admin":
                    if cadastro["idpokedex"]=="admin":
                        self.__controlador_admin.abre_tela()
                        situacao=True
                else:
                    self.__usuario_logado=self.__controlador_admin.valida_treinador(cadastro["usuario"],cadastro["idpokedex"])
                    if not self.__usuario_logado:
                        self.__tela_Login.mostra_mensagem('Dados incorretos')
                    else:
                        situacao = True
                        lista_opcoes = {1: self.gerenciar_pokemons, 2: self.relatorios,0:self.retornar}
                        while True:
                            opcao_escolhida = self.__tela_usuario.tela_opcoes()
                            funcao_escolhida = lista_opcoes[opcao_escolhida]
                            funcao_escolhida()
                            break
            else:
                exit(0)



    def sair(self):
        self.__tela_admin.mostra_mensagem('Programa encerrado com sucesso, volte sempre!')
        exit(0)

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