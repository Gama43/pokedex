class TelaItem:

    def tela_opcoes(self):
        print('-----Opções de Item-----')
        print('1- Adicionar novo item')
        print('2- Alterar item já cadastrado')
        print('3- Remover item')
        print('4- Mostrar itens existentes no mundo')

        opcao = int(input('Sua opção: '))
        return opcao

    def dados_item(self):
        print('-----DADOS NOVO ITEM-----')
        nome = self.nome()
        quantidade = self.quantidade()
        raridade = self.raridade()

        return {"nome": nome, "quantidade": quantidade, "raridade": raridade}

    def mostra_item(self, dados_item):
        print('-------------Item-------------')
        print('NOME DO ITEM: ', dados_item['nome'])
        print('Quantidade: ', dados_item["quantidade"])
        print('RARIDADE: ', dados_item["raridade"])
        print("\n")

    def seleciona_item(self):
        nome = str(input("Nome do item que deseja selecionar: "))
        return nome

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def opcao(self):
        while True:
            try:
                opcao = int(input('Sua opção: '))
            except (TypeError, ValueError):
                print('Digite um valor válido')
                self.menu()
                continue
            else:
                if 0 <= opcao <= 4:
                    return opcao
                else:
                    print('Digite um valor válido')
                    self.menu()
    def menu(self):
        print('-----Opções de Item-----')
        print('1- Adicionar novo item')
        print('2- Alterar item já cadastrado')
        print('3- Remover item')
        print('4- Mostrar itens existentes no mundo')

    def nome(self):
        while True:
            nome = str(input('Nome do Item: '))
            if nome.isalpha() and nome is not None:
                break
        return nome

    def quantidade(self):
        while True:
            quantidade = int(input('Quantidade: '))
            if quantidade is not int and quantidade is not None:
                break
        return quantidade

    def raridade(self):
        while True:
            raridade = int(input('Raridade: '))
            if raridade is not int and raridade is not None:
                break
        return raridade