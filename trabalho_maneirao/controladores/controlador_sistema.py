from view.tela_sistema import TelaSistema
from view.tela_login import TelaLogin
from controladores.controlador_usuario import ControladorUsuario
from controladores.controlador_admin import ControleTreinador
from entidade.treinador import Treinador


class ControladorSistema:


    def __init__(self):
        self.__tela_sistema=TelaSistema()
        self.__tela_Login=TelaLogin()
        self.__controlador_usuario=ControladorUsuario(self)
        self.__controlador_admin=ControleTreinador(self)
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
            if dados_login["usuario"]=="admin" and dados_login["idpokedex"]=="admin":
                self.__controlador_admin.abre_tela()
                situacao=True
            else:
                self.__usuario_logado=self.__controlador_admin.valida_treinador(dados_login["usuario"],dados_login["idpokedex"])
                if not self.__usuario_logado:
                    print('Dados incorretos')
                else:
                    situacao = True
                    self.__controlador_usuario.abre_tela()
                # nome=dados_login['usuario']
                # idpokedex=int(dados_login['idpokedex'])
                # i=self.__controlador_admin.lista_usuarios.index(nome)
                # if self.__controlador_admin.lista_usuarios[i]==nome and self.__controlador_admin.lista_idpokedex[i]==idpokedex:
                #     self.__usuario_logado= self.__controlador_admin.lista_treinadores()
                #     self.__controlador_usuario.abre_tela()
                #     situacao = True

    def teste(self):
        print('teste')












    def abre_tela(self):
        lista_opcoes = {1: self.entrar}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
