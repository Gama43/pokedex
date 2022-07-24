class TelaUsuario:

    def tela_opcoes(self):
        print('--------USUÁRIO--------')
        print('1- Gerenciar pokemons')
        print('2- Relatorios')
        print('0- Retornar')

        opcao = self.opcao()
        return opcao

    def opcao(self):
        while True:
            try:
                opcao=int(input('Sua opção: '))
            except (TypeError,ValueError):
                print('Digite um valor válido')
                self.menu()
                continue
            else:
                if 0<=opcao<=2:
                    return opcao
                else:
                    print('Digite um valor válido')
                    self.menu()
                    continue

    def menu(self):
        print('--------USUÁRIO--------')
        print('1- Gerenciar pokemons')
        print('2- Relatorios')
        print('0- Retornar')

