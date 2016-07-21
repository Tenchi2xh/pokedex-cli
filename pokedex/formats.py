# -*- encoding: utf-8 -*-
from __future__ import print_function

import json as json_lib

from .graphics.cell_buffer import Buffer
from .graphics.draw import *

icon_width = 32
format_names = ["card", "json", "simple", "line", "page"]

def card(pokemon, shiny=False, mega=False):

    evolutions_height = get_height(pokemon.chain.values()[0])
    evolutions_width = get_width(pokemon.chain)
    content_width = max([evolutions_width, len(pokemon.genus) + 3 + 8 + 12, 32])

    icons = pokemon.mega + 1 if mega else 1
    total_icon_width = icons * icon_width

    width = content_width + total_icon_width + 2
    buffer = Buffer(width + 1, 16 + evolutions_height - 2)

    for y in range(buffer.height):
        buffer.put_line((1, y), " " * width, bg=0)

    for mega in range(icons):
        draw_image(buffer, os.path.join(resource_path, pokemon.icon(shiny=shiny, mega=mega)), x0=content_width+1+icon_width*mega)

    buffer.put_line((3, 1), pokemon.name, bg=0)
    buffer.put_line((3, 2), u"%s Pokémon" % pokemon.genus.capitalize(), fg=245, bg=0)
    buffer.put_line((3, 3), "%0.2f m / %0.1f kg" % (pokemon.height / 10.0, pokemon.weight / 10.0), fg=240, bg=0)

    type1 = pokemon.types[0]
    type2 = pokemon.types[1] if len(pokemon.types) > 1 else None

    draw_number(buffer, pokemon.number, bg=0, x0=content_width-12, y0=1)
    draw_type(buffer, type1, type2, x0=3, y0=5)
    draw_flavor_text(buffer, pokemon.flavor, content_width - 3, x0=3, y0=7, bg=0)

    draw_evolutions(buffer, pokemon.chain, pokemon.number, x0=3, y0=13, bg=0)

    buffer.display()


def json(pokemon):
    print(json_lib.dumps({
        "number": pokemon.number,
        "name": pokemon.name,
        "genus": pokemon.genus,
        "flavor": pokemon.flavor,
        "types": pokemon.types,
        "chain": [{"number": stage[0], "name": stage[1]} for stage in pokemon.chain],
        "height": pokemon.height,
        "weight": pokemon.weight
    }, indent=4))


def simple(pokemon):
    print(u"%s (#%03d), %s Pokémon" % (pokemon.name, pokemon.number, pokemon.genus))
    print("%s, %0.2f m, %0.1f kg" % ("/".join(map(lambda s: s.capitalize(), pokemon.types)), pokemon.height / 10.0, pokemon.weight / 10.0))
    print(pokemon.flavor)

    def find_evolutions(chain, ancestor):
        for key in chain.keys():
            if key[0] == pokemon.number:
                return ancestor, chain[key]
            evolutions = find_evolutions(chain[key], ancestor=key)
            if evolutions[0]:
                return evolutions
        return None, []

    ancestor, evolutions = find_evolutions(pokemon.chain, pokemon.chain.keys()[0])
    evolutions = map(lambda e: "%s (#%03d)" % (e[1], e[0]), evolutions)
    if ancestor[1] == pokemon.name:
        ancestor = None
    ancestor = "%s (#%03d)" % (ancestor[1], ancestor[0]) if ancestor else None
    if evolutions or ancestor:
        print("Evolves %s%s%s" % (("from %s" % ancestor) if ancestor else "",
                                  ", and " if ancestor and evolutions else "",
                                  ("into " + ", ".join(evolutions)) if evolutions else ""))


def line(pokemon):
    evolution = " > ".join(["#%03d" % stage[0] for stage in pokemon.chain])
    print(u"%s (#%03d): %s | %s" % (pokemon.name, pokemon.number, "/".join(map(lambda s: s.capitalize(), pokemon.types)), evolution))
