import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.max_hp = 50
        self.alive = True
        self.face = 'G'

    def damage(self):
        return random.random() * 20

gnome = Gnome('Gnome', (12, 7))