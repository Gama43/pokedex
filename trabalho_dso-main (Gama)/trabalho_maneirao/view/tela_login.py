class TelaLogin:

    def tela_login(self):
        print('-----TELA DE LOGIN-----')
        usuario=str(input('Seu usuário: '))
        idpokedex=str(input('Idpokedex: '))
        return {"usuario": usuario, "idpokedex":idpokedex}