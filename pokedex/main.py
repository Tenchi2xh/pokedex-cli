#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"


from .database.get import download_database
from .database.queries import *


def pokedex():
    download_database()
    print get_pokemon_by_id(25)


if __name__ == "__main__":
    pokedex()
