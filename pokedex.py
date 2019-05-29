import requests
import json
import pokemon
from random import randrange

API_BASE = "https://pokeapi.co/api/v2/"

class PokeDex:

    cache = dict()
    count = 0
    berryCount = 0

    def get_pokemon(target):
        """ Return a pokemon entry.

        Check the cache first, else pull the entry from PokeAPI and update the
        cache. Return none if we can't pull data from PokeAPI.

        Arguments:
            - target: a pokemon's name (string)
        """

        target = target.lower()

        if target in PokeDex.cache:
            return PokeDex.cache[target]

        r = requests.get(API_BASE + "pokemon/" + target)
        if not r.ok:
            return None
            
        pokemon_data = json.loads(r.text)
        PokeDex.cache[target] = pokemon.Pokemon(pokemon_data)

        return PokeDex.cache[target]

    def get_random_pokemon():
        """ Get a random pokemon entry.

        Generate a random ID and grab the pokemon related to that ID.
        Update the cache after pulling the data. Return none if we
        can't pull data from PokeAPI.
        """

        if PokeDex.count == 0:

            r = requests.get(API_BASE + "pokemon-species/?limit=0")
            if not r.ok:
                return

            data = json.loads(r.text)
            PokeDex.count = data['count']

        pokeid = randrange(1, PokeDex.count)

        r = requests.get(API_BASE + "pokemon/{}".format(pokeid))
        if not r.ok:
            print(r.ok)
            return

        data = json.loads(r.text)
        PokeDex.cache[data['name']] = pokemon.Pokemon(data)

        return PokeDex.cache[data['name']]

    def get_berry(target):
        """ Return a berry entry.

        Check the cache first, else pull the entry from PokeAPI and update the
        cache. Return none if we can't pull data from PokeAPI.

        Arguments:
            - target: a berry's name (string)
        """

        target = target.lower()

        if target in PokeDex.cache:
            return PokeDex.cache[target]

        r = requests.get(API_BASE + "berry/" + target)
        if not r.ok:
            return None
            
        berry_data = json.loads(r.text)
        PokeDex.cache[target] = pokemon.Berry(berry_data)

        return PokeDex.cache[target]

    def get_random_berry():
        """ Get a random berry entry.

        Generate a random ID and grab the pokemon related to that ID.
        Update the cache after pulling the data. Return none if we
        can't pull data from PokeAPI.
        """

        if PokeDex.berryCount == 0:

            r = requests.get(API_BASE + "berry")
            if not r.ok:
                return

            data = json.loads(r.text)
            PokeDex.berryCount = data['count']

        berryid = randrange(1, PokeDex.berryCount)

        r = requests.get(API_BASE + "berry/{}".format(berryid))
        if not r.ok:
            return

        data = json.loads(r.text)
        PokeDex.cache[data['name']] = pokemon.Berry(data)

        return PokeDex.cache[data['name']]

if __name__ == "__main__":

    target = "pikachu"
    poke = PokeDex.get_pokemon(target)
    print(poke.pokemon_str_rep())
    poke = PokeDex.get_random_pokemon()
    print(poke.pokemon_str_rep())
    print(poke.moves())
    target = "cheri"
    berry = PokeDex.get_berry(target)
    print(berry.berry_str_rep())
    

        
        
