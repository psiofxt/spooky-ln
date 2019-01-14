import pyxel
import random

from models import Skeleton

class App:
    def __init__(self):
        pyxel.init(255, 120, caption='Spooky and Frightening')
        self.player = Skeleton()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_player()

    def update_player(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 1, 1):
            # player is attacking
            self.player.state = 2
            return
        elif self.player.state == 2:
            # player is still in an attack animation
            return
        else:
            # player is idle
            self.player.state = 0

        if pyxel.btn(pyxel.KEY_A):
            # player is moving left
            self.player.state = 1
            self.player.direction = 'left'
            self.player.x = max(self.player.x - 2, 0)
            return

        if pyxel.btn(pyxel.KEY_D):
            # player is moving right
            self.player.state = 1
            self.player.direction = 'right'
            self.player.x = min(self.player.x + 2, pyxel.width - 20)
            return

    def draw(self):
        pyxel.cls(15)
        pyxel.text(0, 0, 'spooky-ln', pyxel.frame_count % 16)
        pyxel.text(0, 0 + 10, f'frame: {pyxel.frame_count}', pyxel.frame_count % 16)

        getattr(self.player, self.player.states[self.player.state])()

App()
