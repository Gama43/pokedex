import PySimpleGUI as sg

class TelaUsuario:
    def __init__(self):
        self.__janela=None
        self.menu()

    def tela_opcoes(self):
        self.menu()
        evento,valores=self.abrir()
        opcao=0
        if valores['pokemons']:
            opcao=1
        if valores['relatorios']:
            opcao=2
        if valores['mochila']:
            opcao=3
        if evento==['voltar']:
            opcao=0


        self.fechar()
        return opcao

    def menu(self):
        layout=[
            [sg.Text('Selcione sua opção',font=50)],
            [sg.Radio('Gerenciar pokemons','opcao', key='pokemons',font=35)],
            [sg.Radio('Relatórios','opcao', key='relatorios',font=35)],
            [sg.Radio('Gerenciar Mochila', 'opcao', key='mochila',font=35)],
            [sg.Button('Continuar', key='opcao', font=35), sg.Button('Voltar', key='voltar', font=35)]
        ]

        self.janela=sg.Window('Tela Usuario').Layout(layout)


    def abrir(self):
        evento, valores=self.janela.Read()
        return evento, valores


    def fechar(self):
        self.janela.Close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg)