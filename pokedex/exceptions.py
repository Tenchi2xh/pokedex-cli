# -*- encoding: utf-8 -*-
 
class NoSuchPokemon(Exception):
    def __init__(self, pokemon):
        super(NoSuchPokemon, self).__init__(u"Pokémon %s not found" % pokemon) 
