import PySimpleGUI as sg

class TelaRelatorios:
    def __init__(self):
        self.__janela=None
        self.menu()


    def tela_opcoes(self):
        self.menu()
        evento, valores = self.abrir()
        opcao = 0
        if valores['alfabetica']:
            opcao = 1
        if valores['nivel']:
            opcao = 2
        if valores['regiao']:
            opcao = 3
        if evento == ['voltar']:
            opcao = 0
        self.fechar()
        return opcao


    def menu(self):
        layout=[
            [sg.Radio('Filtrar por ordem alfabética', 'opcao', key='alfabetica', font=35)],
            [sg.Radio('Filtrar por ordem de nível', 'opcao', key='nivel', font=35)],
            [sg.Radio('Filtrar por região', 'opcao', key='regiao', font=35)],
            [sg.Button('Continuar',key='continuar'), sg.Button('Voltar',key='voltar')]
        ]

        self.janela = sg.Window('Tela relatórios').Layout(layout)

    def abrir(self):
        while True:
            evento, valores=self.janela.Read()
            return evento, valores

    def fechar(self):
        self.janela.Close()

    def mostra_relatorio(self, lista):
        string_total = ""
        for dado in lista:
            string_total = string_total + dado + '\n'

        sg.Popup('---------LISTA Pokemons---------', string_total)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)


    def pega_regiao(self):
        layout = [
            [sg.Text('Regiao do Pokemon')],
            [sg.Radio('Kanto', 'regiao', key='kanto'),
             sg.Radio('Johto', 'regiao', key='johto'), sg.Radio('Hoenn', 'regiao', key='hoenn'),
             sg.Radio('Sinnoh', 'regiao', key='sinnoh')],
            [sg.Radio('Unova', 'regiao', key='unova'), sg.Radio('Kalos', 'regiao', key='kalos'),
             sg.Radio('Alola', 'regiao', key='alola'), sg.Radio('Ilhas Laranja', 'regiao', key='ilhaslaranja')],
            [sg.Button('Continuar', key='continuar')]
        ]

        self.janela = sg.Window('Regiao').Layout(layout)

        evento, valores = self.abrir()
        regiao = ''
        if valores['kanto'] == True:
            regiao = 'kanto'
        if valores['johto'] == True:
            regiao = 'johto'
        if valores['hoenn'] == True:
            regiao = 'hoenn'
        if valores['sinnoh'] == True:
            regiao = 'sinnoh'
        if valores['unova'] == True:
            regiao = 'unova'
        if valores['kalos'] == True:
            regiao = 'kalos'
        if valores['alola'] == True:
            regiao = 'alola'
        if valores['ilhaslaranja'] == True:
            regiao = 'ilhas laranja'
        self.fechar()
        return regiao