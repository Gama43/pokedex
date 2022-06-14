from trabalho_maneirao.view.tela_admin import TelaAdmin
from trabalho_maneirao.entidade.treinador import Treinador

class ControleTreinador:

    def __init__(self, controlador_sistema):
        self.__treinadores = []
        self.__tela_treinador = TelaAdmin()
        self.__controlador_sistema = controlador_sistema
        self.lista_usuarios=[]
        self.lista_idpokedex=[]

    @property
    def treinadores(self):
        return self.__treinadores

    # @property
    # def lista_idpokedex(self):
    #     return self.__idpokedex

    def pega_treinador_por_idpokedex(self, idpokedex: int):
        for treinador in self.__treinadores:
            if (treinador.idpokedex == idpokedex):
                return treinador
        return None

    def adicionar_treinador(self):
        dados_treinador=self.__tela_treinador.dados_treinador()
        nome=dados_treinador["nome"]
        idpokedex=dados_treinador["idpokedex"]
        treinador=Treinador(nome,idpokedex)
        self.__treinadores.append(treinador)
        self.lista_usuarios.append(nome)
        self.lista_idpokedex.append(idpokedex)


    def lista_treinadores(self):
        for treinador in self.__treinadores:
            self.__tela_treinador.mostra_treinador({"nome": treinador.nome, "idpokedex": treinador.idpokedex})


    def alterar_treinador(self):
        self.lista_treinadores()

        idpokedex = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_idpokedex(idpokedex)

        if (treinador is not None):
            novos_dados_treinador = self.__tela_treinador.dados_treinador()
            treinador.nome = novos_dados_treinador["nome"]
            treinador.idpokedex = novos_dados_treinador["idpokedex"]
            self.lista_treinadores()
        else:
            self.__tela_treinador.mostra_mensagem("ATENCAO: Esse treinador não existe")


    def excluir_treinador(self):
        self.lista_treinadores()
        idpokedex = self.__tela_treinador.seleciona_treinador()
        treiandor= self.pega_treinador_por_idpokedex(idpokedex)

        if (treiandor is not None):
            self.__treinadores.remove(treiandor)
            self.lista_treinadores()
        else:
            self.__tela_treinador.mostra_mensagem("ATENCAO: Esse treinador não existe")



    def retornar(self):
        self.__controlador_sistema.entrar()


    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_treinador, 2: self.alterar_treinador, 4: self.excluir_treinador, 3: self.lista_treinadores,
                         0: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_treinador.tela_opcoes()]
            opcao_escolhida()