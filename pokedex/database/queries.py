# -*- coding: utf-8 -*-

import os
import sqlite3

from .. import resource_path


db = sqlite3.connect(os.path.join(resource_path, "veekun-pokedex.sqlite"))
cursor = db.cursor()

def get_versions():
    cursor.execute("""SELECT identifier
                        FROM versions
                   """)
    return [row[0] for row in cursor.fetchall()]

def get_pokemon_by_id(id, language="en", version="x"):
    cursor.execute("""SELECT p.species_id, name, genus, flavor_text
                        FROM pokemon p
                        JOIN languages l ON l.identifier="{language}"
                        JOIN versions v ON v.identifier="{version}"
                        JOIN pokemon_species_names s ON s.local_language_id=l.id AND s.pokemon_species_id=p.species_id
                        JOIN pokemon_species_flavor_text f ON f.language_id=l.id AND f.version_id=v.id AND f.species_id = p.species_id
                       WHERE p.species_id={id}
                   """.format(id=id, language=language, version=version))

    return cursor.fetchall()
