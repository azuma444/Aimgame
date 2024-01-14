import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 12
        self.y = 12
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, 12, 8)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.cls(0)
            self.x = random.randint(12,148)
            self.y = random.randint(12,108)
            pyxel.circ(self.x, self.y, 12, 8)


App()