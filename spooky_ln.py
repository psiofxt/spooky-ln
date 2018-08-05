import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120, caption='Hello')
        self.x = 0
        self.y = 88
        self.direction = 'right'
        self.idle_counter = 1
        self.walk_counter = 1
        self.idling = True
        pyxel.image(0).load(0, 0, 'assets/skeleton/Skeleton Idle.png')
        pyxel.image(1).load(0, 0, 'assets/skeleton/Skeleton Walk.png')

        self.idle_models = {
            1: {
                'sx': 0, 'sy': 0, 'w': 24, 'h': 32, 'col': 0
            },
            2: {
                'sx': 24, 'sy': 0, 'w': 24, 'h': 32, 'col': 0
            },
            3: {
                'sx': 48, 'sy': 0, 'w': 24, 'h': 32, 'col': 0
            },
            4: {
                'sx': 72, 'sy': 0, 'w': 24, 'h': 32, 'col': 0
            },
            5: {
                'sx': 96, 'sy': 0, 'w': 24, 'h': 32, 'col': 0
            },
            6: {
                'sx': 120, 'sy': 0, 'w': 24, 'h': 32, 'col': 0
            },
        }

        self.walk_models = {
            1: {
                'sx': 0, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            2: {
                'sx': 22, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            3: {
                'sx': 44, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            4: {
                'sx': 88, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            5: {
                'sx': 110, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            6: {
                'sx': 132, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            7: {
                'sx': 154, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            8: {
                'sx': 176, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            9: {
                'sx': 198, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            10: {
                'sx': 220, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            11: {
                'sx': 242, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
            12: {
                'sx': 264, 'sy': 0, 'w': 22, 'h': 33, 'col': 0
            },
        }

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_player()

    def update_player(self):
        if pyxel.btnp(pyxel.KEY_LEFT, 10, 1) or pyxel.btnp(pyxel.KEY_RIGHT, 10, 1):
            self.idling = False
        else:
            self.idling = True

        if pyxel.btn(pyxel.KEY_LEFT):
            self.direction = 'left'
            self.x = max(self.x - 2, 0)

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.direction = 'right'
            self.x = min(self.x + 2, pyxel.width - 20)

        """if pyxel.btn(pyxel.KEY_DOWN):
            self.y = max(0, self.y + 2)

        if pyxel.btn(pyxel.KEY_UP):
            self.y = min(self.y - 2, pyxel.height - 8)"""

    def idle(self):
        i = self.idle_counter
        pyxel.blt(self.x, self.y, 0, self.idle_models[i]['sx'],
                  self.idle_models[i]['sy'],
                  self.idle_models[i]['w'] if self.direction == 'right'
                                           else self.idle_models[i]['w'] * -1,
                  self.idle_models[i]['h'], self.idle_models[i]['col'])
        self.idle_counter += 1 if pyxel.frame_count % 4 == 0 else 0
        if self.idle_counter == 7:
            self.idle_counter = 1

    def walk(self):
        i = self.walk_counter
        pyxel.blt(self.x, self.y, 1, self.walk_models[i]['sx'],
                  self.walk_models[i]['sy'],
                  self.walk_models[i]['w'] if self.direction == 'right'
                                           else self.walk_models[i]['w'] * -1,
                  self.walk_models[i]['h'], self.walk_models[i]['col'])
        self.walk_counter += 1 if pyxel.frame_count % 2 == 0 else 0
        if self.walk_counter == 11:
            self.walk_counter = 1

    def draw(self):
        pyxel.cls(13)
        pyxel.text(55, 41, 'spooky-ln', pyxel.frame_count % 16)
        pyxel.text(55, 41 + 10, f'frame: {pyxel.frame_count}', pyxel.frame_count % 16)
        self.idle() if self.idling else self.walk()

App()
