import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = random.randint(12,148)
        self.y = random.randint(12,108)
        pyxel.circ(random.randint(12,148), random.randint(12,108), 12, 8)

    def draw(self):
        pyxel.cls(0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.cls(0)
            pyxel.circ(random.randint(12,148), random.randint(12,108), 12, 8)


App()