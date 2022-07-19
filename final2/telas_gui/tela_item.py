import PySimpleGui as sg

class TelaItem:
    def __init__(self):
        self.janela = None
        self.menu()

    def tela_opcoes(self):
        self.menu()
        evento,valores = self.abrir()
        opcao = 0
        if valores['Adicionar']:
            opcao = 1
        if valores['Alterar']:
            opcao = 2
        if valores['Remover']:
            opcao = 3
        if valores['Listar']:
            opcao = 4
        if evento == ['voltar'] or evento in (None, 'Cancelar'):
            opcao = 0

        self.fechar()
        return opcao

    def menu(self):
        layout = [
            [sg.Text('Selecione sua opção', font = 50)],
            [sg.Radio('Adicionar Item', key='Adicionar', font=35)],
            [sg.Radio('Alterar Item', key='Alterar', font=35)],
            [sg.Radio('Excluir Item', key='Remover', font=35)],
            [sg.Radio('Mostrar itens existentes no mundo', key='Listar', font=35)],
            [sg.Buttton('Continuar', key='opcao', font=35), sg.Cancel('Cancelar', font=35)]
        ]
        self.janela = sg.Window('Tela Item').Layout(layout)

    def abrir(self):
        evento, valores = self.janela.Read()
        return evento, valores

    def fechar(self):
        self.janela.Close()

    def dados_item(self):
        layout = [
            [sg.Text('Dados do Novo Item')],
            [sg.Text('Nome do Item: ', size=12), sg.Input(size=20, key='nome')],
            [sg.Text('Quantidade: ', size=12), sg.Input(size=20, key='quantidade')],
            [sg.Text('Raridade: ', size=12), sg.Slider(range=(1, 5), oriention='h', size=(5,20), default_value=1, key="raridade")],
            [sg.Button('Continuar', key='continuar'), sg.Button('Voltar', key='voltar')]
        ]

        self.janela = sg.Window('Tela Item').Layout(layout)

        evento, valores = self.abrir()
        nome = valores['nome']
        quantidade = valores['quantidade']
        raridade = valores['raridade']
        self.fechar()
        if evento == 'continuar':
            return {'nome': nome, 'quantidade': quantidade, 'raridade': raridade}
        else:
            return None

    def mostrar_item(self):
        string_total = ""
        for dado in dados_itens:
            string_total = string_total + 'Nome: ' + str(dado['nome']) + '\n'
            string_total = string_total + 'Idpokedex: ' + str(dado['idpokedex']) + '\n'
   
    def mostra_mensagem(self, msg):
        sg.popup("", msg)
        

        sg.Popup('---------LISTA ITENS---------', string_total)

    def nome_item(self):
        layout = [
            [sg.Text('Nome do Item')],
            [sg.Text('Nome', size=12), sg.Input(size=20, key='nome')],
            [sg.Button('Continuar', key='continuar'), sg.Button('Voltar', key='voltar')]
        ]

        self.janela = sg.Window('Tela Nome_item').Layout(layout)

        evento, valores = self.abrir()
        nome = valores['nome']
        self.fechar()
        return nome
