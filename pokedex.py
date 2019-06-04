import requests
import json
import pokemon
from random import randrange

API_BASE = "https://pokeapi.co/api/v2"

class PokeDex:

    cache = dict()
    pokemonCount = 0
    berryCount = 0
    abilityCount = 0

    def get_entry(entryType, target):
        """ Return a PokeDex entry.

        Check the cache first, else pull the entry from PokeAPI and update the
        cache. Return none if we can't pull data from PokeAPI.

        Arguments:
            - entryType: "pokemon", "ability", or "berry" 
            - target: an entry's name or ID (string)
        """

        target = target.lower()

        if target in PokeDex.cache:
            return PokeDex.cache[target]

        r = requests.get("{}/{}/{}".format(API_BASE, entryType, target))
        if not r.ok:
            return None
            
        data = json.loads(r.text)

        if entryType == "ability":
            PokeDex.cache[target] = pokemon.Ability(data)
        elif entryType == "berry":
            PokeDex.cache[target] = pokemon.Berry(data)
        elif entryType == "pokemon":
            PokeDex.cache[target] = pokemon.Pokemon(data)

        return PokeDex.cache[target]

    def get_random_entry(entryType):
        """ Get a random PokeDex entry.

        Generate a random ID and grab the entity related to that ID.
        Update the cache after pulling the data. Return none if we
        can't pull data from PokeAPI.
        """

        if entryType == "ability" and PokeDex.abilityCount == 0:

            r = requests.get(API_BASE + "/ability")
            if not r.ok:
                print("POKEAPI: Request Failure")
                return

            data = json.loads(r.text)
            PokeDex.abilityCount = data['count']

            entryID = randrange(1, PokeDex.berryCount)
        elif entryType == "berry" and PokeDex.berryCount == 0:

            r = requests.get(API_BASE + "/berry")
            if not r.ok:
                print("POKEAPI: Request Failure")
                return

            data = json.loads(r.text)
            PokeDex.berryCount = data['count']

            entryID = randrange(1, PokeDex.berryCount)
        elif entryType == "pokemon" and PokeDex.pokemonCount == 0:

            r = requests.get(API_BASE + "/pokemon-species/?limit=0")
            if not r.ok:
                print("POKEAPI: Request Failure")
                return

            data = json.loads(r.text)
            PokeDex.pokemonCount = data['count']

            entryID = randrange(1, PokeDex.pokemonCount)            

        r = requests.get(API_BASE + "/{}/{}".format(entryType, entryID))
        if not r.ok:
            print("POKEAPI: Request Failure")
            return

        data = json.loads(r.text)
        
        if entryType == "ability":
            PokeDex.cache[data['name']] = pokemon.Ability(data)
        elif entryType == "berry":
            PokeDex.cache[data['name']] = pokemon.Berry(data)
        elif entryType == "pokemon":
            PokeDex.cache[data['name']] = pokemon.Pokemon(data)

        return PokeDex.cache[data['name']]

    def get_pokemon_sound(target):
        """Return the link to the target pokemon's cry

        Check the cache and try to pull the ID for that pokemon or
        pull the entry from PokeAPI and update the cache. We MUST use
        the PokeID (not the name) to get the sound. Return a link to
        the sound.

        Arguments:
            - target: an entry's name or ID(string)
        """

        target = target.lower()

        if not target in PokeDex.cache:
            r = requests.get("{}/{}/{}".format(API_BASE, "pokemon", target))
            if not r.ok:
                return None

            data = json.loads(r.text)
            PokeDex.cache[target] = pokemon.Pokemon(data)

        targetID = PokeDex.cache[target].ID

        return pokemon.PokeSound(targetID).get_link()
    
if __name__ == "__main__":

    target = "pikachu"
    poke = PokeDex.get_entry("pokemon", target)
    print(poke.pokemon_str_rep())
    poke = PokeDex.get_random_entry("pokemon")
    print(poke.pokemon_str_rep())
    print(poke.moves())
    target = "cheri"
    berry = PokeDex.get_entry("berry", target)
    print(berry.berry_str_rep())
    

        
        
