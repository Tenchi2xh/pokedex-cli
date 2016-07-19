#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

import click

from .database.get import download_database
from .graphics.draw import draw_card
from .exceptions import *

__version__ = "0.1.2"


@click.command()
@click.argument("pokemon")
@click.option("-s", "--shiny", is_flag=True, help=u"Show shiny version of the Pokémon.")
@click.option("-m", "--mega", is_flag=True, help=u"Show Mega Evolution(s) if available.")
@click.option("-l", "--language", metavar="LANGUAGE", default="en", help=u"Pokédex language to use.")
@click.option("-pv", "--pokedex-version", metavar="VERSION", default="x", help=u"Pokédex version to use.")
def pokedex(pokemon, shiny, mega, language, pokedex_version):
    """Command-line interface for a quick Pokédex reference.

    Positional argument POKEMON can be either an id or a name, which has to be
    specified in the configured language.
    """
    download_database()
    from .pokemon import Pokemon

    buffer = draw_card(Pokemon(pokemon, language=language, version=pokedex_version), shiny=shiny, mega=mega)
    buffer.display()

if __name__ == "__main__":
    pokedex()
