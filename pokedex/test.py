from .graphics import draw
from .graphics.cell_buffer import Buffer

from .main import resource_path

b = Buffer()
draw.draw_image(os.path.join(resource_path, "icons/icon006.png", b)

for line in b.render():
    print line