class TelaUsuario:

    def tela_usuario(self):
        print('--------USUÁRIO--------')
        print('1- Capturar pokemon')
        print('2- Listrar pokemon')
        print('3- Alterar pokemon')
        print('4- Excluir pokemon')
        print('5- Evoluir pokemon')
        print('6- Abrir mochila')
        print('7- Relatorios')
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
                if 0<=opcao<=7:
                    return opcao
                else:
                    print('Digite um valor válido')
                    self.menu()
                    continue

    def menu(self):
        print('--------USUÁRIO--------')
        print('1- Capturar pokemon')
        print('2- Listrar pokemon')
        print('3- Alterar pokemon')
        print('4- Excluir pokemon')
        print('5- Evoluir pokemon')
        print('6- Abrir mochila')
        print('7- Relatorios')
        print('0- Retornar')

    def tela_relatorios(self):
        print('--------------RELATÓRIOS--------------')
        print('1- Filtrar por ordem alfabetica')
        print('2- Filtrar por ordem de nivel')
        print('3- Filtrar por regiao')
        print('0- Retornar')
        opcao=self.opcao2()
        return opcao

    def opcao2(self):
        while True:
            try:
                opcao = int(input('Sua opção: '))
            except (TypeError, ValueError):
                print('Digite um valor válido')
                self.tela_relatorios()
                continue
            else:
                if 0 <= opcao <= 3:
                    return opcao
                else:
                    print('Digite um valor válido')
                    self.tela_relatorios()
                    continue