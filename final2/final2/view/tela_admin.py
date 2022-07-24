class TelaAdmin:

    def tela_opcoes(self):
        print('----------------ADMIN----------------')
        print('1- Cadastrar treinador')
        print('2- Alterar treinador')
        print('3- Listar treinador')
        print('4- Excluir treinador')
        print('5- Ver todos os pokemons registrados no sistema')
        print('6- Pesquisar pokemon por nome')
        print('7- Gerenciar itens')
        print('0- Retornar')

        opcao = self.opcao()
        return opcao

    def dados_treinador(self):
        print('-----DADOS TREINADOR-----')
        nome=self.nome()
        idpokedex=self.idpokedex()
        return {"nome":nome, "idpokedex":idpokedex}

    def mostra_treinador(self, dados_treinador):
        print('-------------TREINADOR------------- ')
        print("NOME DO TREINADOR: ", dados_treinador["nome"])
        print("IDPOKEDEX DO TREINADOR: ", dados_treinador["idpokedex"])
        print("\n")


    def seleciona_treinador(self):
        idpokedex = self.idpokedex()
        return idpokedex

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
                if 0 <= opcao <= 7:
                    return opcao
                else:
                    print('Digite um valor válido')
                    self.menu()
                    continue

    def menu(self):
        print('----------------ADMIN----------------')
        print('1- Cadastrar treinador')
        print('2- Alterar treinador')
        print('3- Listar treinador')
        print('4- Excluir treinador')
        print('5- Ver todos os pokemons registrados no sistema')
        print('6- Pesquisar pokemon por nome')
        print('7- Gerenciar itens')
        print('0- Retornar')

    def nome(self):
        while True:
            nome=str(input('Nome do treinador: '))
            if nome.isalpha() and nome is not None:
                    break
        return nome

    def idpokedex(self):
        while True:
            idpokdex=str(input('Idpokedex: '))
            if idpokdex.isnumeric() and idpokdex is not None:
                    break
        return int(idpokdex)