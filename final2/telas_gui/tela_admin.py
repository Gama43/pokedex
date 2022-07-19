import PySimpleGUI as sg

class TelaAdmin:
    def __init__(self):
        self.janela=None
        self.menu()


    def tela_opcoes(self):
        self.menu()
        evento,valores=self.abrir()
        opcao=0
        if valores['incluir']:
            opcao=1
        if valores['excluir']:
            opcao=2
        if valores['alterar']:
            opcao=3
        if valores['listar']:
            opcao=4
        if valores['pokemons']:
            opcao=5
        if valores['itens']:
            opcao=6
        if valores['pokemon_nome']:
            opcao=7
        if evento==['voltar'] or evento in (None, 'voltar'):
            opcao=0


        self.fechar()
        return opcao


    def menu(self):
        layout=[
            [sg.Text('Selcione sua opção',font=50)],
            [sg.Radio('Incluir Treinador','opcao', key='incluir',font=35)],
            [sg.Radio('Excluir Treinador','opcao', key='excluir',font=35)],
            [sg.Radio('Alterar Treinador', 'opcao', key='alterar',font=35)],
            [sg.Radio('Listar Treinadores', 'opcao', key='listar',font=35)],
            [sg.Radio('Ver todos os pokemons registrados no sistema','opcao',key='pokemons',font=35)],
            [sg.Radio('Gerenciar itens', 'opcao', key='itens',font=35)],
            [sg.Radio('Pesquisar pokemon por nome', 'opcao', key='pokemon_nome',font=35)],
            [sg.Button('Continuar',key='opcao',font=35),sg.Cancel('voltar',font=35)]
        ]
        self.janela=sg.Window('Tela admin').Layout(layout)


    def abrir(self):
        evento, valores=self.janela.Read()
        return evento, valores

    def fechar(self):
        self.janela.Close()

    def dados_treinador(self):
        layout = [
            [sg.Text('Dados Treinador')],
            [sg.Text('Nome',size=12), sg.Input(size=20, key='nome')],
            [sg.Text('Idpokedex',size=12), sg.Input(size=20, key='idpokedex')],
            [sg.Button('Continuar', key='continuar'), sg.Button('Voltar',key='voltar')]
        ]

        self.janela = sg.Window('Tela admin').Layout(layout)

        evento,valores=self.abrir()
        if evento=='voltar':
            self.fechar()
            return 'voltar'
        nome=valores['nome']
        idpokedex=valores['idpokedex']
        self.fechar()
        if evento=='continuar':
            return {'nome':nome,'idpokedex':idpokedex}
        else:
            return None


    def mostra_treinador(self,dados_treianador):
        string_total=""
        for dado in dados_treianador:
            string_total = string_total + 'Nome: ' + str(dado['nome'])+'\n'
            string_total = string_total + 'Idpokedex: ' + str(dado['idpokedex']) + '\n'

        sg.Popup('---------LISTA TREINADORES---------',string_total)



    def id_treinador(self):
        layout = [
            [sg.Text('IDPOKEDEX do Treinador')],
            [sg.Text('Idpokedex', size=12), sg.Input(size=20, key='idpokedex')],
            [sg.Button('Continuar', key='continuar'), sg.Button('Voltar', key='voltar')]
        ]

        self.janela = sg.Window('Tela idpokedex').Layout(layout)

        evento, valores = self.abrir()
        idpokedex = valores['idpokedex']
        self.fechar()
        return idpokedex

    def mostra_mensagem(self, msg):
        sg.popup("", msg)