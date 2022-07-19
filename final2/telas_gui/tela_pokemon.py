import PySimpleGUI as sg

class TelaPokemon:
    def __init__(self):
        self.janela=None
        self.menu()


    def tela_opcoes(self):
        self.menu()
        evento,valores=self.abrir()
        opcao=0
        if valores['capturar']:
            opcao=1
        if valores['excluir']:
            opcao=2
        if valores['alterar']:
            opcao=3
        if valores['listar']:
            opcao=4
        if valores['evoluir']:
            opcao=5
        if evento==['voltar']:
            opcao=0
        self.fechar()
        return opcao

    def menu(self):
        layout = [
            [sg.Radio('Capturar pokemon', 'opcao', key='capturar', font=35)],
            [sg.Radio('Excluir pokemon', 'opcao', key='excluir', font=35)],
            [sg.Radio('Alterar pokemon', 'opcao', key='alterar', font=35)],
            [sg.Radio('Listar pokemon', 'opcao', key='listar', font=35)],
            [sg.Radio('Evoluir pokemon', 'opcao', key='evoluir', font=35)],
            [sg.Button('Continuar'), sg.Button('Voltar', key='voltar')]
        ]

        self.janela = sg.Window('Gerenciar pokemons').Layout(layout)


    def abrir(self):
        evento, valores=self.janela.Read()
        return evento, valores

    def fechar(self):
        self.janela.Close()

    def dados_pokemon(self):
        layout = [
            [sg.Text('Nome', size=16), sg.Input(size=20, key='nome')],
            [sg.Text('Tipo', size=16), sg.Input(size=20, key='tipo')],
            [sg.Text('Level', size=16), sg.Input(size=20, key='level')],
            [sg.Text('Nome do ataque 1', size=16), sg.Input(size=20, key='nomeataque1')],
            [sg.Text('Valor do ataque 1', size=16), sg.Input(size=20, key='valorataque1')],
            [sg.Text('Nome do ataque 2', size=16), sg.Input(size=20, key='nomeataque2')],
            [sg.Text('Valor do ataque 2', size=16), sg.Input(size=20, key='valorataque2')],
            [sg.Text('Defesa', size=16), sg.Input(size=20, key='defesa')],
            [sg.Text('Região', size=16), sg.Input(size=20, key='regiao')],
            [sg.Button('OK', key='continuar'), sg.Button('Cancelar', key='cancelar')]
        ]
        self.janela = sg.Window('Dados Pokemon').Layout(layout)

        evento,valores=self.abrir()
        if evento=='cancelar':
            self.fechar()
            return 'cancelar'
        nome=valores['nome']
        tipo=valores['tipo']
        level=valores['level']
        nomeataque1=valores['nomeataque1']
        nomeataque2 = valores['nomeataque2']
        valorataque1=valores['valorataque1']
        valorataque2 = valores['valorataque2']
        defesa=valores['defesa']
        regiao=valores['regiao']

        self.fechar()
        if evento=='continuar':
            return {'nome':nome,'tipo': tipo,'level':level, 'nomeataque1':nomeataque1,'valorataque1':valorataque1,'nomeataque2':nomeataque2,'valorataque2':valorataque2,'defesa':defesa,'regiao':regiao}
        else:
            return None


    def mostra_pokemon(self,dados_pokemons):
        string_total=""
        for dado in dados_pokemons:
            string_total = string_total + 'Nome: ' + str(dado['nome'])+'\n'
            string_total = string_total + 'Idpokedex: ' + str(dado['idpokedex']) + '\n'

        sg.Popup('---------LISTA TREINADORES---------',string_total)


    def nome_pokemon(self):
        layout = [
            [sg.Text('Nome do Pokemon')],
            [sg.Text('Pokemon', size=12), sg.Input(size=20, key='nome')],
            [sg.Button('Continuar', key='continuar'), sg.Button('Voltar', key='voltar')]
        ]

        self.janela = sg.Window('Nome').Layout(layout)

        evento, valores = self.abrir()
        nome = valores['nome']
        self.fechar()
        return nome

    def mostra_mensagem(self, msg):
        sg.popup("", msg)