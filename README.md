![](https://img.shields.io/github/tag/Tenchi2xh/pokedex-cli.svg)

# Pokédex CLI

The Pocket Monster Index, now in your terminal!

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Acknowledgments](#acknowledgments)

## Installation

```
pip install "git+git://github.com/Tenchi2xh/pokedex-cli.git@v0.1.4#egg=pokedex-cli"
```

## Usage

```
$ pokedex --help
Usage: main.py [OPTIONS] POKEMON

  Command-line interface for a quick Pokédex reference.

  Positional argument POKEMON can be either an id or a name, which has to be
  specified in the configured language.

Options:
  -s, --shiny                     Show shiny version of the Pokémon.
  -m, --mega                      Show Mega Evolution(s) if available.
  -l, --language LANGUAGE         Pokédex language to use.
  -pv, --pokedex-version VERSION  Pokédex version to use.
  -f, --format FORMAT             Output format (can be card, json, simple,
                                  line, page).
  --help                          Show this message and exit.
```

## Screenshots

<img width="527" alt="screen shot 2016-07-18 at 21 58 44" src="https://cloud.githubusercontent.com/assets/4116708/16928557/a648e8ce-4d33-11e6-9234-f76b8a1ef720.png">
<img width="485" alt="screen shot 2016-07-18 at 22 01 08" src="https://cloud.githubusercontent.com/assets/4116708/16928550/9effd960-4d33-11e6-8f28-04ac185595db.png">
<img width="500" alt="screen shot 2016-07-18 at 22 03 53" src="https://cloud.githubusercontent.com/assets/4116708/16928547/9b4c0f64-4d33-11e6-8143-b285790ea4bc.png">

## Acknowledgments

- Database fetched at runtime from [Veekun](http://veekun.com/dex/downloads)
- Icons adapted from [Pikachumazzinga on DeviantArt](http://pikachumazzinga.deviantart.com/art/Pokemon-Essentials-Icon-Pack-ORAS-UPDATE-424114559)

Pokémon © 2002-2016 Pokémon. © 1995-2016 Nintendo/Creatures Inc./GAME FREAK inc. TM, ® and Pokémon character names are trademarks of Nintendo.

No copyright or trademark infringement is intended in using Pokémon content in this project.
