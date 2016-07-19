# -*- encoding: utf-8 -*-

import os

from .exceptions import *
from .database.queries import *

class Pokemon(object):
    def __init__(self, pokemon, language=default_language, version=default_version):
        try:
            self.number = get_pokemon_id(pokemon, language=language)
            results = get_pokedex_entry(self.number, language=language, version=version)
            if len(results) == 0:
                # TODO: Separate exception for "No entry for this version/language combo"
                raise NoSuchPokemon(pokemon)
        except NoSuchPokemon:
            self.number = 0
            self.name   = "MISSINGNO."
            self.genus  = "???"
            self.flavor = u"Pokémon %s not found" % pokemon
            self.types  = ["flying", "normal"]
            self.chain  = [(0, "MISSINGNO.")]
            self.height = 10
            self.weight = 100
        else:
            entry = results[0]
            self.number = entry[0]
            self.name   = entry[1]
            self.genus  = entry[2]
            self.flavor = entry[3].replace("\n", " ").replace("\f", " ")
            self.types  = get_pokemon_type(self.number)
            self.chain  = get_pokemon_evolution_chain(self.number, language=language)
            self.height = entry[4]
            self.weight = entry[5]

    def icon(self, shiny=False, mega=0):
        mega_suffix = ["", "_mega", "_mega_1"][mega]
        return "icons/icon%03d%s%s.png" % (self.number, "s" if shiny else "", mega_suffix)

    @property
    def mega(self):
        if os.path.isfile(os.path.join(resource_path, self.icon(mega=2))):
            return 2
        if os.path.isfile(os.path.join(resource_path, self.icon(mega=1))):
            return 1
        return 0