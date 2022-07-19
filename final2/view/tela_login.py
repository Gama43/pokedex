class TelaLogin:

    def tela_login(self):
        print('-------TELA DE LOGIN-------')
        usuario=self.usuario()
        idpokedex=self.idpokedex()
        #print('Para sair:'
              #'Usuario=sair
              #'Idpokedex=123')
        return {"usuario": usuario, "idpokedex":idpokedex}


    def usuario(self):
        while True:
            usuario=str(input('Seu usuario: '))
            if usuario and usuario.isalpha():
                return usuario
            else:
                continue

    def idpokedex(self):
        while True:
            idpokedex=str(input('Seu idpokedex: '))
            if idpokedex:
                return idpokedex
            else:
                continue