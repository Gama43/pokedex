from entidade.pokemon import Pokemon
from entidade.pokemon_evoluido import PokemonEvoluido
from telas_gui.tela_pokemon import TelaPokemon
from valor_nulo_exception import ValorNuloException
from não_eh_string import NaoEhString


class ControladorPokemon():

    def __init__(self,controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__tela_pokemon=TelaPokemon()
        self.__pokemons=[]



    def capturar_pokemon(self):
        sit=True
        dados_pokemon = self.__tela_pokemon.dados_pokemon()
        if dados_pokemon=='cancelar':
            self.abre_tela()
        nome = dados_pokemon["nome"]
        if len(nome)==0:
            raise ValorNuloException
        if nome.isalpha()==False:
            raise NaoEhString

        tipo = dados_pokemon["tipo"]
        level = dados_pokemon["level"]

        nomeataque1 = dados_pokemon["nomeataque1"]
        if len(nomeataque1)==0:
            raise ValorNuloException
        if nomeataque1.isalpha()==False:
            raise NaoEhString
        valorataque1=dados_pokemon['valorataque1']
        nomeataque2=dados_pokemon['nomeataque2']
        if len(nomeataque2)==0:
            raise ValorNuloException
        if nomeataque2.isalpha()==False:
            raise NaoEhString
        valorataque2 = dados_pokemon['valorataque2']
        ataques = [{nomeataque1: valorataque1},{nomeataque2:valorataque2}]
        defesa = dados_pokemon["defesa"]
        regiao = dados_pokemon["regiao"]
        pokemon_pra_adicionar = Pokemon(nome, tipo, level, ataques, defesa, regiao)

        cont=0
        for pokemon in self.__pokemons:
            if pokemon.nome==nome:
                cont+=1
        if cont==0:
            if sit is True:
                self.__controlador_sistema.usuario_logado.lista_pokemons.append(pokemon_pra_adicionar)
        else:
            self.__tela_pokemon.mostra_mensagem('Erro! Esse treinador ja cadastrou esse pokemon!')


    def lista_pokemons(self):
        sit=True
        dados_pokemon=[]
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            dados_pokemon.append({"nome": pokemon.nome, "tipo": pokemon.tipo,"level": pokemon.level, "ataques": pokemon.ataques, "defesa": pokemon.defesa, "regiao": pokemon.regiao})
            sit=False
        if sit:
            self.__tela_pokemon.mostra_mensagem('Esse treinador ainda não capturou pokemons')
        else:
            self.__tela_pokemon.mostra_pokemon(dados_pokemon)

    def seleciona_pokemon_por_nome(self,nome):
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            if (pokemon.nome == nome):
                return pokemon
        return None


    def alterar_pokemon(self):
        sit=False
        nome_pokemon = self.__tela_pokemon.nome_pokemon()
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

        nome_pokemon = self.__tela_pokemon.nome_pokemon()
        pokemon=self.seleciona_pokemon_por_nome(nome_pokemon)
        if pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            self.__controlador_sistema.usuario_logado.lista_pokemons.remove(pokemon)

        else:
            self.__tela_pokemon.mostra_mensagem('Pokemon não encontrado')


    def evoluir_pokemon(self):
        nome=self.__tela_pokemon.nome_pokemon()
        sit=False
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:

            if pokemon.nome==nome:
                sit=True
                if pokemon.level>=18:
                    novo_pokemon=PokemonEvoluido(pokemon.nome,pokemon.tipo,pokemon.level,pokemon.ataques,
                                            pokemon.defesa,pokemon.regiao)
                    novo_ataque=self.__tela_pokemon.ataque_pokemon_evoluido()
                    novo_pokemon.ataques.append(novo_ataque)
                    self.__controlador_sistema.usuario_logado.lista_pokemons.append(novo_pokemon)
                    self.__controlador_sistema.usuario_logado.lista_pokemons.remove(pokemon)
                else:
                    self.__tela_pokemon.mostra_mensagem(f"Para evoluir, o pokemon deve estar no mínimo\n no level 18, e atualmente ele está no level {pokemon.level}")
        if sit==False:
            self.__tela_pokemon.mostra_mensagem("Esse pokemon ainda não foi capturado")

    def retornar(self):
        self.__controlador_sistema.tela()

    def abre_tela(self):
        lista_opcoes = {1: self.capturar_pokemon, 3:self.alterar_pokemon,4:self.lista_pokemons,2:self.excluir_pokemon,5:self.evoluir_pokemon, 0:self.retornar}
        while True:
            opcao_escolhida = self.__tela_pokemon.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()