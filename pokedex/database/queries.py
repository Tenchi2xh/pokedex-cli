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


def get_types():
    cursor.execute("""SELECT type_id, name
                        FROM type_names
                       WHERE type_id < 10000 AND local_language_id=9
                   """)
    return {row[0]: row[1].lower() for row in cursor.fetchall()}


def get_pokemon_id(pokemon, language=default_language):
    try:
        pokemon_id = int(pokemon)
        if pokemon_id <= 0 or pokemon_id > 721:
            raise NoSuchPokemon("#%d" % pokemon_id)
        return pokemon_id
    except ValueError:
        return get_pokemon_by_name(pokemon, language=language)


def get_pokemon_name(id, language=default_language):
    cursor.execute("""SELECT name
                        FROM pokemon_species_names s
                        JOIN languages l ON l.identifier="{language}"
                       WHERE s.local_language_id=l.id AND s.pokemon_species_id={id}
                   """.format(id=id, language=language))
    return cursor.fetchall()[0][0]


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


def get_pokemon_type(pokemon_id):
    all_types = get_types()
    cursor.execute("""SELECT type_id, slot
                        FROM pokemon_types
                       WHERE pokemon_id={pokemon_id}
                   """.format(pokemon_id=pokemon_id))
    types = sorted([(row[0], int(row[1])) for row in cursor.fetchall()], key=lambda t: t[1])
    return map(lambda t: all_types[t[0]], types)


def get_pokemon_evolution_chain(pokemon_id, language=default_language):
    cursor.execute("""SELECT id, evolves_from_species_id
                        FROM pokemon_species
                       WHERE evolution_chain_id = (SELECT evolution_chain_id FROM pokemon_species WHERE id={pokemon_id})
                   """.format(pokemon_id=pokemon_id))
    chain = [(row[0], get_pokemon_name(row[0], language), row[1]) for row in cursor.fetchall()]
    root = (pkmn for pkmn in chain if pkmn[2] is None).__next__()
    tree = {root: {}}
    del chain[chain.index(root)]

    def add_evolutions(tree, root, chain):
        evolutions = [pkmn for pkmn in chain if pkmn[2] == root[0]]
        for evolution in evolutions:
            tree[root][evolution] = {}
            del chain[chain.index(evolution)]
            add_evolutions(tree[root], evolution, chain)

    add_evolutions(tree, root, chain)

    return tree


def get_pokedex_entry(id, language=default_language, version=default_version):
    cursor.execute("""SELECT p.species_id, name, genus, flavor_text, height, weight
                        FROM pokemon p
                        JOIN languages l ON l.identifier="{language}"
                        JOIN versions v ON v.identifier="{version}"
                        JOIN pokemon_species_names s ON s.local_language_id=l.id AND s.pokemon_species_id=p.species_id
                        JOIN pokemon_species_flavor_text f ON f.language_id=l.id AND f.version_id=v.id AND f.species_id = p.species_id
                       WHERE p.species_id={id}
                   """.format(id=id, language=language, version=version))

    return cursor.fetchall()
