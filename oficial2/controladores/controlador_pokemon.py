from oficial2.entidade.pokemon import Pokemon
from oficial2.entidade.pokemon_evoluido import PokemonEvoluido
from oficial2.view.tela_pokemon import TelaPokemon



class ControladorPokemon():

    def __init__(self,controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__tela_pokemon=TelaPokemon()
        self.__pokemons=[]



    def capturar_pokemon(self):
        dados_pokemon = self.__tela_pokemon.dados_pokemon()
        nome = dados_pokemon["nome"]
        tipo = dados_pokemon["tipo"]
        level = dados_pokemon["level"]
        ataques = dados_pokemon["ataques"]
        defesa = dados_pokemon["defesa"]
        regiao = dados_pokemon["regiao"]
        pokemon_pra_adicionar = Pokemon(nome, tipo, level, ataques, defesa, regiao)
        cont=0
        for pokemon in self.__pokemons:
            if pokemon.nome==nome:
                cont+=1
        if cont==0:
            self.__controlador_sistema.usuario_logado.lista_pokemons.append(pokemon_pra_adicionar)
        else:
            self.__tela_pokemon.mostra_mensagem('Erro! Esse treinador ja cadastrou esse pokemon!')


    def lista_pokemons(self):
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            self.__tela_pokemon.mostra_pokemon({"nome": pokemon.nome, "tipo": pokemon.tipo,"level": pokemon.level, "ataques": pokemon.ataques, "defesa": pokemon.defesa, "regiao": pokemon.regiao})


    def seleciona_pokemon_por_nome(self,nome):
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            if (pokemon.nome == nome):
                return pokemon
        return None


    def alterar_pokemon(self):
        self.lista_pokemons()
        sit=False
        nome_pokemon = self.__tela_pokemon.seleciona_pokemon()
        pokemon=self.seleciona_pokemon_por_nome(nome_pokemon)
        if (pokemon is not None):
            for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
                if pokemon.nome==nome_pokemon:
                    sit=True
                    novos_dados_pokemon = self.__tela_pokemon.dados_pokemon()
                    pokemon.nome = novos_dados_pokemon["nome"]
                    pokemon.tipo = novos_dados_pokemon["tipo"]
                    pokemon.level = novos_dados_pokemon["level"]
                    pokemon.ataques = novos_dados_pokemon["ataques"]
                    pokemon.defesa = novos_dados_pokemon["defesa"]
                    pokemon.regiao = novos_dados_pokemon["regiao"]
                    self.lista_pokemons()
        if sit==False:
            self.__tela_pokemon.mostra_mensagem('Esse pokemon não foi capturado')

    def excluir_pokemon(self):
        self.lista_pokemons()
        nome_pokemon = self.__tela_pokemon.seleciona_pokemon()
        pokemon=self.seleciona_pokemon_por_nome(nome_pokemon)
        if pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            self.__controlador_sistema.usuario_logado.lista_pokemons.remove(pokemon)

        else:
            self.__tela_pokemon.mostra_mensagem('Pokemon não encontrado')


    def evoluir_pokemon(self):
        nome=self.__tela_pokemon.seleciona_pokemon()
        sit=False
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:

            if pokemon.nome==nome:
                sit=True
                if pokemon.level>=18:
                    novo_pokemon=PokemonEvoluido(pokemon.nome,pokemon.tipo,pokemon.level,pokemon.ataques,
                                            pokemon.defesa,pokemon.regiao)
                    self.__controlador_sistema.usuario_logado.lista_pokemons.append(novo_pokemon)
                    self.__controlador_sistema.usuario_logado.lista_pokemons.remove(pokemon)
                else:
                    self.__tela_pokemon.mostra_mensagem(f"Para evoluir, o pokemon deve estar no mínimo\n no level 18, e atualmente ele está no level {pokemon.level}")
        if sit==False:
            self.__tela_pokemon.mostra_mensagem("Esse pokemon ainda não foi capturado")

    def retornar(self):
        self.__controlador_sistema.tela()

    def abre_tela(self):
        lista_opcoes = {1: self.capturar_pokemon, 2:self.alterar_pokemon,3:self.lista_pokemons,4:self.alterar_pokemon,5:self.evoluir_pokemon, 0:self.retornar}
        while True:
            opcao_escolhida = self.__tela_pokemon.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()