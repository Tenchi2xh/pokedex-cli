# -*- coding: utf-8 -*-

from PIL import Image

from .colors import rgb_to_xterm

block_top = "▀"

def draw_image(path, buffer, x0=0, y0=0):
    image = Image.open(path).convert("RGB")
    pixels = image.load()
    width, height = image.size

    for y in range(0, height, 2):
        for x in range(width):
            if x + x0 < buffer.width and y + y0 < buffer.height * 2:
                color_top = rgb_to_xterm(pixels[x, y])
                color_bottom = rgb_to_xterm(pixels[x, y + 1])

                buffer.put_cell((x, y // 2), u"▀", color_top, color_bottom)
