import requests
import json

class Pokemon:

    def __init__(self, data):
        """Build a Pokemon class from the PokeDex data from PokeAPI"""
        self.ID = data['id']
        self._name = data['name']
        self._height = data['height']
        self._init_stats(data)
        self._init_types(data)
        self._init_moves(data)
        self._weight = data['weight']
        self._sprite = data['sprites']['front_default']
        
    def _init_stats(self, data):

        self._stats = dict()

        num = len(data['stats'])
        for i in range(num):    
            self._stats[data['stats'][i]['stat']['name'].capitalize()] = data['stats'][i]['base_stat']

    def _init_types(self, data):

        self._types = []

        num = len(data['types'])
        for i in range(num):
            self._types.append(data['types'][i]['type']['name'].capitalize())

    def _init_moves(self, data):

        self._moves = []
        
        num = len(data['moves'])
        for i in range(num):
            self._moves.append(data['moves'][i]['move']['name'].capitalize())
            
    def pokemon_str_rep(self):

        result = self._name.capitalize() + ":\n"
        result += "    Height: {}\n    Weight: {}\n".format(self._height, self._weight)
        result += "    Types:\n"
        for value in self._types:
            result += "        - {}\n".format(value.capitalize())

        result += "    Base Stats:\n"
            
        for key, value in self._stats.items():
            result += "        - {}: {}\n".format(key, value)

        result += "    Usable/Learnable Moves:\n"
            
        for value in self._moves:
            result += "        - {}\n".format(value)

        return result

    def types(self):

        result = "Types:\n"
        for value in self._types:
            result += "    - {}\n".format(value)

        return result

    def stats(self):

        result = "Base Stats:\n"
            
        for key, value in self._stats.items():
            result += "    - {}: {}\n".format(key, value)

        return result

    def moves(self):
        
        result = "Usable/Learnable Moves:\n"
            
        for value in self._moves:
            result += "    - {}\n".format(value)

        return result

    def name(self):
        return self._name.capitalize() + ":\n"

    def name_stripped(self):
        return self._name

    def height(self):
        return "Height: {} m\n".format(self._height / 10)

    def weight(self):
        return "Weight: {0:.2f} lbs.\n".format(self._weight * 2.205 / 10)

    def sprite_link(self):
        return self._sprite

class Berry:

    def __init__(self, data):
        """Build a Berry class from the PokeDex data from PokeAPI"""
        self._name = data['name']
        self._firmness = data['firmness']['name']
        self._size = data['size']
        self._init_flavors(data)
        self._grab_data(data)
        
    def _init_flavors(self, data):

        self._flavors = []

        num = len(data['flavors'])
        for i in range(num):
            self._flavors.append(data['flavors'][i]['flavor']['name'].capitalize())

    def _grab_data(self, data):

        r = requests.get(data['item']['url'])
        if not r.ok:
                return

        data2 = json.loads(r.text)
        self._effect = data2['effect_entries'][0]['effect']
        self._sprite = data2['sprites']['default']
            
    def berry_str_rep(self):

        result = self._name.capitalize() + ":\n"
        result += "    Size: {} cm\n    Firmness: {}\n".format(self._size / 10, self._firmness)
        result += "    Effect: {}\n".format(self._effect)
        result += "    Flavors:\n"
        for value in self._flavors:
            result += "        - {}\n".format(value)

        return result

    def flavors(self):

        result = "Flavors:\n"
        for value in self._flavors:
            result += "    - {}\n".format(value)

        return result

    def name(self):
        return self._name.capitalize() + ":\n"

    def name_stripped(self):
        return self._name

    def size(self):
        return "Size: {} cm\n".format(self._size / 10)

    def firmness(self):
        return "Firmness: {}\n".format(self._firmness)

    def effect(self):
        return "Effect: {}\n\n".format(self._effect)

    def sprite_link(self):
        return self._sprite

class Ability:

    def __init__(self, data):
        """Build an Ability class from the PokeDex data from PokeAPI"""

        self._name = data['name']
        self._generation = data['generation']['name']
        self._effect = data['effect_entries'][0]['effect']

    def str_rep(self):

        result = self._name.capitalize() + ":\n"
        result += "Generation: {}\n".format(self._generation)
        result += "Effect: {}\n".format(self._effect)

        return result

class PokeSound:

    URL_BASE = "https://pokemoncries.com/cries/"

    def __init__(self, pokeID):
        self._ID = pokeID
        self._audioType = ".mp3"

    def get_link(self):
        return PokeSound.URL_BASE + str(self._ID) + self._audioType

        
    
