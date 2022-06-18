from trabalho_maneirao.view.tela_usuario import TelaUsuario
from trabalho_maneirao.view.tela_login import TelaLogin
from trabalho_maneirao.view.tela_pokemon import TelaPokemon
from trabalho_maneirao.entidade.pokemon import Pokemon
from trabalho_maneirao.entidade.pokemon_evoluido import PokemonEvoluido
from trabalho_maneirao.controladores.controlador_admin import ControleTreinador


class ControladorUsuario():

    def __init__(self,controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__tela_pokemon=TelaPokemon()
        self.__tela_login=TelaLogin()
        self.__tela_usuario=TelaUsuario()
        self.__controlador_treinadores=ControleTreinador(self)


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
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            if pokemon.nome==nome:
                cont+=1
        if cont==0:
            self.__controlador_sistema.usuario_logado.lista_pokemons.append(pokemon_pra_adicionar)
        else:
            print('Erro! Esse treinador ja cadastrou esse pokemon!')


    def lista_pokemons(self):
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            self.__tela_pokemon.mostra_pokemon({"nome": pokemon.nome, "tipo": pokemon.tipo,"level": pokemon.level, "ataques": pokemon.ataques, "defesa": pokemon.defesa, "regiao": pokemon.regiao})


    def alterar_pokemon(self):
        self.lista_pokemons()
        nome_pokemon = self.__tela_pokemon.seleciona_pokemon()
        pokemon=self.seleciona_pokemon_por_nome(nome_pokemon)
        if (pokemon is not None):
            novos_dados_pokemon = self.__tela_pokemon.dados_pokemon()
            pokemon.nome = novos_dados_pokemon["nome"]
            pokemon.tipo = novos_dados_pokemon["tipo"]
            pokemon.level = novos_dados_pokemon["level"]
            pokemon.ataques = novos_dados_pokemon["ataques"]
            pokemon.defesa = novos_dados_pokemon["defesa"]
            pokemon.regiao = novos_dados_pokemon["regiao"]
            self.lista_pokemons()


    def excluir_pokemon(self):
        self.lista_pokemons()
        nome_pokemon = self.__tela_pokemon.seleciona_pokemon()
        pokemon=self.seleciona_pokemon_por_nome(nome_pokemon)
        if pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            self.__controlador_sistema.usuario_logado.lista_pokemons.remove(pokemon)
        else:
            print('Pokemon não encontrado')


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



    def ver_mochila(self):
        pass

    def seleciona_pokemon_por_nome(self,nome):
        for pokemon in self.__controlador_sistema.usuario_logado.lista_pokemons:
            if (pokemon.nome == nome):
                return pokemon
        return None


    def relatorios(self):
        self.abre_tela_relatorios()


    def retornar(self):
        self.__controlador_sistema.entrar()


    def abre_tela(self):
        lista_opcoes = {1: self.capturar_pokemon, 2: self.lista_pokemons,3:self.alterar_pokemon,4:self.excluir_pokemon,5:self.evoluir_pokemon,6:self.ver_mochila,7:self.relatorios, 0:self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_usuario.tela_usuario()]
            opcao_escolhida()


    def abre_tela_relatorios(self):
        lista_opcoes = {1: self.listar_ordem_alfabetica,2:self.listar_nivel_crescente,3:self.listar_regiao,0: self.retornar2}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_usuario.tela_relatorios()]
            opcao_escolhida()


    def listar_ordem_alfabetica(self):
        print('-' * 32)
        lista_nomes = []
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_nomes.append(pokemon.nome)
        lista_nomes.sort()
        c = 1
        for nome in lista_nomes:
            print(f'Pokemon Nº{c}: {nome}')
            print('-'*32)
            c+=1
        print('\n')


    def listar_nivel_crescente(self):
        print('-' * 32)
        lista_levels=[]
        lista_printados=[]
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_levels.append(pokemon.level)
        lista_levels.sort()
        i=1
        for level in lista_levels:
            for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
                if pokemon.level==level and pokemon not in lista_printados:
                    print(f'Pokemon Nº{i}: {pokemon.nome}/ Nível: {pokemon.level}')
                    print('-' * 32)
                    lista_printados.append(pokemon)
                    i+=1
        print('\n')


    def listar_regiao(self):
        print('-' * 32)
        regiao=self.__tela_pokemon.regiao()
        lista_regioes=[]
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            lista_regioes.append(pokemon.regiao)
        print(f'Pokemons da região: {regiao}')
        c = 0
        for pokemon in (self.__controlador_sistema.usuario_logado.lista_pokemons):
            if pokemon.regiao==regiao:
                c+=1
                print(f'Pokemon Nº{c}: {pokemon.nome}')
        if regiao not in lista_regioes:
            print(f'Não foram cadastrados pokemons em {regiao}.')


    def retornar2(self):
        self.abre_tela()


