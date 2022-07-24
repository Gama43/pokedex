import PySimpleGUI as sg
from valor_invalido_exception import ValorInvalidoException

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
            [sg.Text('Nome', size=16), sg.Input(size=20, key='nome',default_text=None)],
            [sg.Text('Tipo', size=16), sg.Radio('Elétrico','tipo',key='eletrico'),sg.Radio('Fantasma','tipo',key='fantasma'),sg.Radio('Fogo','tipo',key='fogo'),sg.Radio('Grama','tipo',key='grama')],
            [sg.Text(' ',size=16),sg.Radio('Água','tipo',key='agua'),sg.Radio('Fada','tipo',key='fada'),sg.Radio('Normal','tipo',key='normal'),sg.Radio('Psiquico','tipo',key='psiquico')],
            [sg.Text('Level', size=16), sg.Slider(range=(1, 100), orientation='h', key='level')],
            [sg.Text('')],
            [sg.Text('Nome do ataque 1', size=16), sg.Input(size=20, key='nomeataque1')],
            [sg.Text('Valor do ataque 1', size=16), sg.Slider(range=(1, 100), orientation='h',key='valorataque1')],
            [sg.Text('')],
            [sg.Text('Nome do ataque 2', size=16), sg.Input(size=20, key='nomeataque2')],
            [sg.Text('Valor do ataque 2', size=16), sg.Slider(range=(1, 100), orientation='h',key='valorataque2')],
            [sg.Text('')],
            [sg.Text('Defesa', size=16), sg.Slider(range=(1, 100), orientation='h',key='defesa')],
            [sg.Text('Região', size=16), sg.Radio('Kanto','regiao',key='kanto'),sg.Radio('Johto','regiao',key='johto'),sg.Radio('Hoenn','regiao',key='hoenn'),sg.Radio('Sinnoh','regiao',key='sinnoh')],
            [sg.Text(' ', size=16), sg.Radio('Unova', 'regiao', key='unova'), sg.Radio('Kalos', 'regiao', key='kalos'),
             sg.Radio('Alola', 'regiao', key='alola'), sg.Radio('Ilhas Laranja', 'regiao', key='ilhaslaranja')],
            [sg.Button('OK', key='continuar'), sg.Button('Cancelar', key='cancelar')]
        ]
        self.janela = sg.Window('Dados Pokemon').Layout(layout)
        sit=True
        evento,valores=self.abrir()
        if evento=='cancelar':
            self.fechar()
            return 'cancelar'
        while True:
            nome = valores['nome']

            break

        level=valores['level']
        nomeataque1=valores['nomeataque1']
        nomeataque2 = valores['nomeataque2']
        valorataque1=valores['valorataque1']
        valorataque2 = valores['valorataque2']
        defesa=valores['defesa']
        tipo=''
        if valores['eletrico']==True:
            tipo='Elétrico'
        if valores['fantasma']==True:
            tipo='fantasma'
        if valores['fogo']==True:
            tipo='fogo'
        if valores['grama']==True:
            tipo='grama'
        if valores['agua']==True:
            tipo='agua'
        if valores['fada']==True:
            tipo='fada'
        if valores['normal']==True:
            tipo='normal'
        if valores['psiquico']==True:
            tipo='psiquico'
        regiao=''
        if valores['kanto']==True:
            regiao='kanto'
        if valores['johto']==True:
            regiao='johto'
        if valores['hoenn']==True:
            regiao='hoenn'
        if valores['sinnoh']==True:
            regiao='sinnoh'
        if valores['unova']==True:
            regiao='unova'
        if valores['kalos']==True:
            regiao='kalos'
        if valores['alola']==True:
            regiao='alola'
        if valores['ilhaslaranja']==True:
            regiao='ilhas laranja'



        self.fechar()
        if evento=='continuar' and sit:
            return {'nome':nome,'tipo': tipo,'level':level, 'nomeataque1':nomeataque1,'valorataque1':valorataque1,'nomeataque2':nomeataque2,'valorataque2':valorataque2,'defesa':defesa,'regiao':regiao}
        else:
            return None


    def mostra_pokemon(self,dados_pokemons):
        string_total=""
        for dado in dados_pokemons:
            string_total = string_total + 'Nome: ' + str(dado['nome'])+'\n'
            string_total = string_total + 'Tipo: ' + str(dado['tipo']) + '\n'
            string_total = string_total + 'Level: ' + str(dado['level']) + '\n'
            string_total = string_total + 'Ataques: ' + str(dado['ataques']) + '\n'
            string_total = string_total + 'Defesa: ' + str(dado['defesa']) + '\n'
            string_total = string_total + 'Regiao: ' + str(dado['regiao']) + '\n'

        sg.Popup('---------LISTA Pokemon---------',string_total)


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

    def ataque_pokemon_evoluido(self):
        layout = [
                [sg.Text('Novo ataque', size=16)],
                [sg.Text('Nome do ataque', size=16), sg.Input(size=20, key='nomeataque')],
                [sg.Text('Valor do ataque', size=16), sg.Slider(range=(1, 100), orientation='h',key='valorataque')],
                [sg.Button('Continuar', key='continuar')]
            ]

        self.janela = sg.Window('Ataques').Layout(layout)

        evento, valores = self.abrir()
        nomeataque = valores['nomeataque']
        valorataque=valores['valorataque']
        ataque={nomeataque:valorataque}
        self.fechar()
        return ataque
