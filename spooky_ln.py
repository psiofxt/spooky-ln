import pyxel
import random

from models import Skeleton

class App:
    def __init__(self):
        pyxel.init(160, 120, caption='Spooky and Frightening')
        self.player = Skeleton()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_player()

    def update_player(self):
        if pyxel.btnp(pyxel.KEY_LEFT, 10, 1) or pyxel.btnp(pyxel.KEY_RIGHT, 10, 1):
            self.player.idling = False
        else:
            self.player.idling = True

        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.direction = 'left'
            self.player.x = max(self.player.x - 2, 0)

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.direction = 'right'
            self.player.x = min(self.player.x + 2, pyxel.width - 20)

    def draw(self):
        pyxel.cls(13)
        pyxel.text(55, 41, 'spooky-ln', pyxel.frame_count % 16)
        pyxel.text(55, 41 + 10, f'frame: {pyxel.frame_count}', pyxel.frame_count % 16)
        self.player.idle() if self.player.idling else self.player.walk()

App()
