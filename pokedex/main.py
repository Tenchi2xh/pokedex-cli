#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

import click

from .database.get import download_database
from .database.queries import *
from .graphics.draw import draw_card
from .exceptions import *

__version__ = "0.2.0"


@click.command()
@click.argument("pokemon")
@click.option("-l", "--language", metavar="LANGUAGE", default="en", help=u"Pokédex language to use")
@click.option("-pv", "--pokedex-version", metavar="VERSION", default="x", help=u"Pokédex version to use")
def main(pokemon, language, pokedex_version):
    """Command-line interface for a quick Pokédex reference.

    Positional argument POKEMON can be either an id or a name, which has to be
    specified in the configured language.
    """
    download_database()

    # TODO: catch exception, generate MISSINGNO 
    try:
        pokemon_id = get_pokemon_id(pokemon, language=language)
    except NoSuchPokemon:
        buffer = draw_card("MISSINGNO.", 0, "???", ["flying", "normal"], u"Pokémon %s not found" % pokemon, 10, 100, [], "icons/icon000.png")
    else:
        entry = get_pokedex_entry(pokemon_id, language=language, version=pokedex_version)[0]
        icon_path = "icons/icon%03d.png" % int(entry[0])
        evolution_chain = get_pokemon_evolution_chain(pokemon_id, language=language)
        types = get_pokemon_type(pokemon_id)
        buffer = draw_card(entry[1], int(entry[0]), entry[2], types, entry[3], entry[4], entry[5], evolution_chain, icon_path)

    buffer.display()

if __name__ == "__main__":
    main()
