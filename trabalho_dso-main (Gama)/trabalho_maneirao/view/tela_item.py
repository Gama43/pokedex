class TelaItem:

    def tela_item(self):
        print('-----DADOS NOVO ITEM-----')
        nome = str(input('NOME do novo item: '))
        quantidade = int(input('Quantidade: '))
        raridade = int(input('raridade: '))

        return {"nome": nome, "quantidade": quantidade, "raridade": raridade}