import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = 'G'

    def damage(self):
        return random.random() * 20