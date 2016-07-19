#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

import click

from .database.get import download_database
from .exceptions import *
from . import formats

__version__ = "0.1.4"


@click.command()
@click.argument("pokemon")
@click.option("-s", "--shiny", is_flag=True, help=u"Show shiny version of the Pokémon.")
@click.option("-m", "--mega", is_flag=True, help=u"Show Mega Evolution(s) if available.")
@click.option("-l", "--language", metavar="LANGUAGE", default="en", help=u"Pokédex language to use.")
@click.option("-pv", "--pokedex-version", metavar="VERSION", default="x", help=u"Pokédex version to use.")
@click.option("-f", "--format", metavar="FORMAT", default="card", type=click.Choice(formats.format_names), help="Output format (can be %s)." % ", ".join(formats.format_names))
def pokedex(pokemon, shiny, mega, language, pokedex_version, format):
    """Command-line interface for a quick Pokédex reference.

    Positional argument POKEMON can be either an id or a name, which has to be
    specified in the configured language.
    """
    download_database()
    from .pokemon import Pokemon

    pkmn = Pokemon(pokemon, language=language, version=pokedex_version)
    if format == "card":
        formats.card(pkmn, shiny=shiny, mega=mega)
    elif format == "page":
        pass
    else:
        getattr(formats, format)(pkmn)

if __name__ == "__main__":
    pokedex()
