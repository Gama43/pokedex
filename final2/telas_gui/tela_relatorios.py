import PySimpleGUI as sg

class TelaRelatorios:
    def __init__(self):
        layout=[
            [sg.Radio('Filtrar por ordem alfabética', 'opcao', key='alfabetica', font=35)],
            [sg.Radio('Filtrar por ordem de nível', 'opcao', key='nivel', font=35)],
            [sg.Radio('Filtrar por região', 'opcao', key='regiao', font=35)],
            [sg.Button('Continuar',key='continuar'), sg.Button('Excluir',key='excluir')]
        ]

        self.janela = sg.Window('Gerenciar pokemons').Layout(layout)

    def abrir(self):
        while True:
            evento, valores=self.janela.Read()
            return evento, valores
