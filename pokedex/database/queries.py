# -*- coding: utf-8 -*-

import os
import sqlite3

from .. import resource_path
from ..exceptions import *

db = sqlite3.connect(os.path.join(resource_path, "veekun-pokedex.sqlite"))
cursor = db.cursor()

default_version = "x"
default_language = "en"

def get_versions():
    cursor.execute("""SELECT identifier
                        FROM versions
                   """)
    return [row[0] for row in cursor.fetchall()]

def get_pokemon_id(pokemon, language=default_language):
    try:
        pokemon_id = int(pokemon)
        return pokemon_id
    except ValueError:
        return get_pokemon_by_name(pokemon, language=language)

def get_pokemon_by_name(name, language=default_language):
    cursor.execute("""SELECT p.species_id
                        FROM pokemon p
                        JOIN languages l ON l.identifier="{language}"
                        JOIN pokemon_species_names s ON s.local_language_id=l.id AND LOWER(s.name)="{name}"
                       WHERE p.species_id=s.pokemon_species_id
                   """.format(name=name.lower().strip(), language=language))

    rows = cursor.fetchall()
    if len(rows) == 0:
        raise NoSuchPokemon(name)
    return rows[0][0]

def get_pokedex_entry(id, language=default_language, version=default_version):
    cursor.execute("""SELECT p.species_id, name, genus, flavor_text
                        FROM pokemon p
                        JOIN languages l ON l.identifier="{language}"
                        JOIN versions v ON v.identifier="{version}"
                        JOIN pokemon_species_names s ON s.local_language_id=l.id AND s.pokemon_species_id=p.species_id
                        JOIN pokemon_species_flavor_text f ON f.language_id=l.id AND f.version_id=v.id AND f.species_id = p.species_id
                       WHERE p.species_id={id}
                   """.format(id=id, language=language, version=version))

    return cursor.fetchall()
