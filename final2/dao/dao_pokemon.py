from dao.dao_abstract import DAO
from entidade.pokemon import Pokemon


class PokemonDAO(DAO):
    def __init__(self):
        super().__init__('pokemon.pkl')

    def add(self, pokemon: Pokemon):
        if (isinstance(pokemon.nome, str) and (pokemon is not None)) \
                and isinstance(pokemon, Pokemon):
            super().adicionar(pokemon.nome, pokemon)

    def get(self, chave: str):
        if isinstance(chave, str):
            return super().get(chave)

    def remove(self, chave: str):
        return super().remove(chave)