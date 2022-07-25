import PySimpleGUI as sg

class TelaLogin:
    def __init__(self):
        self.__janela=None


    def dados_login(self):
        layout=[
            [sg.Text('Usuario',size=10),sg.Input(key='usuario')],
            [sg.Text('IDpokedex',size=10),sg.Input(key='idpokedex')],
            [sg.Button('Login',key='login'), sg.Button('Sair',key='sair')]
        ]

        self.__janela=sg.Window('Tela de login').layout(layout)

        evento,valores=self.abrir()
        if evento=='sair' or sg.WIN_CLOSED:
            self.__janela.close()

        usuario=valores['usuario']
        idpokdedex=str(valores['idpokedex'])
        self.fechar()
        if evento=='login':
            return{'usuario':usuario,'idpokedex':idpokdedex}
        else:
            return None


    def fechar(self):
        self.__janela.Close()


    def abrir(self):
        evento, valores = self.__janela.Read()
        return evento, valores

    def mostra_mensagem(self, msg):
        sg.popup("", msg)