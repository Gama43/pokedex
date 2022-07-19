class TelaRelatorio:

    def tela_relatorios(self):
        print('--------------RELATÓRIOS--------------')
        print('1- Filtrar por ordem alfabetica')
        print('2- Filtrar por ordem de nivel')
        print('3- Filtrar por regiao')
        print('0- Retornar')
        opcao = self.opcao()
        return opcao

    def opcao(self):
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