import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = random.randint(0,160)
        self.y = random.randint(0,120)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.exists = False

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 5)

App()