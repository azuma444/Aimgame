import pyxel
import random


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.score = 0
        self.R = 0
        self.x = 12
        self.y = 12
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if 0 <= self.score <= 20:
            self.R = 12
        elif 21 <= self.score <= 40:
            self.R = 9
        elif 41 <= self.score <= 70:
            self.R = 6
        elif 71 <= self.score:
            self.R = 3

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, f'score {self.score}', 7)

        pyxel.circ(self.x, self.y, self.R, 8)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.x-self.R <= pyxel.mouse_x <= self.x+self.R and self.y-self.R <= pyxel.mouse_y <= self.y+self.R:
            pyxel.cls(0)
            self.score += 1
            self.x = random.randint(12,148)
            self.y = random.randint(12,108)
            pyxel.circ(self.x, self.y, self.R, 8)

App()