#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"


from database.get import download_database


def pokedex():
    download_database()


if __name__ == "__main__":
    pokedex()
