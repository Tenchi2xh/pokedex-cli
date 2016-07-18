#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

import click

from .database.get import download_database
from .database.queries import *

__version__ = "0.1.0"


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

    pokemon_id = get_pokemon_id(pokemon, language=language)

    print(get_pokedex_entry(pokemon_id, language=language, version=pokedex_version))


if __name__ == "__main__":
    main()
