from trabalho_maneirao.view.tela_sistema import TelaSistema
from trabalho_maneirao.view.tela_login import TelaLogin
from trabalho_maneirao.controladores.controlador_usuario import ControladorUsuario
from trabalho_maneirao.controladores.controlador_admin import ControleTreinador
from trabalho_maneirao.entidade.treinador import Treinador


class ControladorSistema:


    def __init__(self):
        self.__tela_sistema=TelaSistema()
        self.__tela_Login=TelaLogin()
        self.__controlador_usuario=ControladorUsuario(self)
        self.__controlador_admin=ControleTreinador(self)


    def inicializa_sistema(self):
        self.abre_tela()


    def entrar(self):
        situacao = False
        while situacao == False:
            dados_login = self.__tela_Login.tela_login()
            if dados_login["usuario"]=="admin" and dados_login["idpokedex"]=="admin":
                self.__controlador_admin.abre_tela()
                situacao=True
            else:
                nome=dados_login['usuario']
                idpokedex=int(dados_login['idpokedex'])
                i=self.__controlador_admin.lista_usuarios.index(nome)
                if self.__controlador_admin.lista_usuarios[i]==nome and self.__controlador_admin.lista_idpokedex[i]==idpokedex:
                    self.__controlador_usuario.abre_tela()
                    situacao = True
                else:
                    print('Dados incorretos')













    def abre_tela(self):
        lista_opcoes = {1: self.entrar}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()