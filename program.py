import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load(images.pyxres)
        self.x = random.randint(0,160)
        self.y = random.randint(0,120)
        self.exists = True
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.exists = False

        if self.exists == False:
            return

    def draw(self):
        pyxel.cls(0)
        if self.exists == False:
            return
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 5)

App()

