# -*- coding: utf-8 -*-

from .conversion import rgb2short

def rgb_to_xterm(color):
    hex_color = "%02x%02x%02x" % color
    return int(rgb2short(hex_color)[0])

reset_code = "\033[0m"

def format_fg(fg):
    return "\033[38;5;%dm" % fg

def format_bg(bg):
    if bg == -1:
        return "\033[49m"
    return "\033[48;5;%dm" % bg

def format_color(text, fg=15, bg=0):
    fg_code = format_fg(fg)
    bg_code = format_bg(bg)
    return fg_code + bg_code + text + reset_code