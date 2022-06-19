class TelaMochila:

    def tela_opcoes(self):
        print('-----MOCHILA-----')
        print('1- Adicionar Item na Mochila')
        print('2- Excluir Item da Mochila')
        print('3- Mostrar Itens na Mochila')
        print('0- Retornar')

        opcao = self.opcao()
        return opcao

    def opcao(self):
        while True:
            try:
                opcao = int(input('Sua opcão'))
            except (TypeError, ValueError):
                print('Digite um valor válido')
                self.menu()
                continue
            else:
                if 0 <= opcao <= 3:
                    return opcao
                else:
                    print('Digite um valor válido')
                    self.menu()
                    continue

    def menu(self):
        print('-----MOCHILA-----')
        print('1- Adicionar Item na Mochila')
        print('2- Excluir Item da Mochila')
        print('3- Mostrar Itens na Mochila')
        print('0- Retornar')

    def seleciona_item(self):
        opcao = int(input("Digite uma opção: "))
        return opcao