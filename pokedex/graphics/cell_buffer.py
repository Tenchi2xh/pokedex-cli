# -*- coding: utf-8 -*-

from .colors import *

import collections


Cell = collections.namedtuple('Cell', 'character fg bg')


class Buffer(object):
    def __init__(self, width=80, height=16):
        self.width = width
        self.height = height
        self.buffer = [[Cell(" ", 15, -1) for x in range(width)] for y in range(height)]

    def put_cell(self, position, character, fg=15, bg=-1):
        x, y = position
        assert x >= 0
        assert y >= 0
        assert x < self.width
        assert y < self.height

        assert type(character) in (str, unicode)
        if len(character) == 0:
            character = " "

        self.buffer[y][x] = Cell(character, fg, bg)

    def render(self):
        output = []
        for line in self.buffer:
            result = ""
            last_fg, last_bg = -1, -1

            for cell in line:
                if cell.fg != last_fg:
                    result += format_fg(cell.fg)
                    last_fg = cell.fg
                if cell.bg != last_bg:
                    result += format_bg(cell.bg)
                    last_bg = cell.bg
                result += cell.character
            result += reset_code
            output.append(result)

        return output