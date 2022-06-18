
class TelaPokemon:

    def dados_pokemon(self):
        print('-------DADOS POKEMON-------')
        nome = self.nome()
        tipo = self.tipo()
        level = self.level()
        ataques = self.ataques()
        defesa = self.defesa()
        regiao = self.regiao()
        return {"nome": nome, "tipo": tipo,
                "level": level, "ataques": ataques, "defesa": defesa, "regiao": regiao}


    def mostra_pokemon(self, dados_pokemon):

        print(f'----------Pokemon---------- ')
        print("Nome do POKEMON: ", dados_pokemon["nome"])
        print("Tipo do POKEMON: ", dados_pokemon["tipo"])
        print("Level do POKEMON: ", dados_pokemon["level"])
        print("Ataques do POKEMON: ", dados_pokemon["ataques"])
        print("Defesa so POKEMON: ", dados_pokemon["defesa"])
        print("Regiao do POKEMON: ", dados_pokemon["regiao"])
        print("\n")


    def seleciona_pokemon(self):
        while True:
            nome=input("Nome do pokemon que deseja selecionar: ")
            if nome and not nome.isnumeric():
                return nome
            else:
                continue
        return nome

    def nome(self):
        while True:
            nome=str(input('Nome do pokemon: ')).lower().strip()
            if nome and not nome.isnumeric():
                return nome
            else:
                continue

    def tipo(self):
        while True:
            tipo=str(input('Tipo do pokemon: '))
            if tipo and not tipo.isnumeric():
                return tipo
            else:
                continue

    def level(self):
        while True:
            try:
                level=int(input('Level do pokemon: '))
                if level and type(level)==int:
                    return level
                else:
                    continue
            except ValueError:
                continue

    def defesa(self):
        while True:
            try:
                defesa=int(input('Defesa do pokemon: '))
                if defesa and type(defesa)==int:
                    return defesa
                else:
                    continue
            except ValueError:
                continue

    def regiao(self):
        while True:
            regiao=str(input('Regiao do pokemon: '))
            if regiao and not regiao.isnumeric():
                return regiao
            else:
                continue

    def nome_ataque(self,indice):
        while True:
            nome_ataque = str(input(f'Nome do ataque {indice}: '))
            if nome_ataque and not nome_ataque.isnumeric():
                return nome_ataque
            else:
                continue

    def valor_ataque(self,indice):
        while True:
            try:
                valor_ataque = int(input(f'Valor do ataque {indice}: '))
                if valor_ataque and type(valor_ataque) == int:
                    return valor_ataque
                else:
                    continue
            except ValueError:
                continue

    def ataques(self):
        self.__ataques=[]
        for c in range(1,3):
            nome_ataque=self.nome_ataque(c)
            valor_ataque=self.valor_ataque(c)
            ataque={nome_ataque: valor_ataque}
            self.__ataques.append(ataque)
        return self.__ataques

    def mostra_mensagem(self, mensagem):
        print(mensagem)