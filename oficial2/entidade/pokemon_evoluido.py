from oficial2.entidade.pokemon import Pokemon

class PokemonEvoluido(Pokemon):
    def __init__(self,nome,tipo,level,ataques,defesa,regiao):
        super().__init__(nome+ ' EX',tipo,level,ataques,defesa*2,regiao)
        ataque3=self.nome_ataque()
        valor3=self.valor_ataque()
        ataques.append({ataque3:valor3})

    def nome_ataque(self):
        while True:
            nome_ataque = str(input(f'Nome do ataque 3: '))
            if nome_ataque and nome_ataque.isalpha():
                return nome_ataque
            else:
                continue

    def valor_ataque(self):
        while True:
            try:
                valor_ataque = int(input(f'Valor do ataque 3: '))
                if valor_ataque and type(valor_ataque) == int:
                    return valor_ataque
                else:
                    continue
            except ValueError:
                continue