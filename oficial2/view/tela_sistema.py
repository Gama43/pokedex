class TelaSistema:

    def tela_opcoes(self):
        print('-------SISTEMA-------')
        print('1- ENTRAR')
        print('2- ENCERRAR PROGRAMA')

        opcao=self.opcao()
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
                if 1<=opcao<=2:
                    return opcao
                else:
                    print('Digite um valor válido')
                    self.menu()
                    continue


    def menu(self):
        print('-------SISTEMA-------')
        print('1- ENTRAR')
        print('2- ENCERRAR PROGRAMA')