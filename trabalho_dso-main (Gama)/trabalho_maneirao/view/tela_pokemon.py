from trabalho_maneirao.entidade.ataques_pokemon import AtaquesPokemon
class TelaPokemon:

    def dados_pokemon(self):
        print('-----DADOS POKEMON-----')
        nome = str(input('NOME do Pokemon: '))
        tipo = str(input('Tipo: '))
        level = int(input('Level: '))
        ataques = AtaquesPokemon().ataques
        defesa = int(input('Defesa: '))
        regiao = str(input('Regiao: '))
        return {"nome": nome, "tipo": tipo,
                "level": level, "ataques": ataques, "defesa": defesa, "regiao": regiao}


    def mostra_pokemon(self, dados_pokemon):
        print("Nome do POKEMON: ", dados_pokemon["nome"])
        print("Tipo do POKEMON: ", dados_pokemon["tipo"])
        print("Level do POKEMON: ", dados_pokemon["level"])
        print("Ataques do POKEMON: ", dados_pokemon["ataques"])
        print("Defesa DO POKEMON: ", dados_pokemon["defesa"])
        print("Regiao DO POKEMON: ", dados_pokemon["regiao"])
        print("\n")


    def seleciona_pokemon(self):
        nome = input("Nome do pokemon que deseja selecionar: ")
        return nome