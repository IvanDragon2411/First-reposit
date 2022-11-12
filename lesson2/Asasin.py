from Fight.Charter import Charecter
import random
class Asasin(Charecter):

    def __init__(self, name='', health=100, damage=1, live=True):
        Charecter.__init__(self, name, health, damage, live)

    def attack(self, target):
        addd_damge = 0
        if random.randint(1, 100) <= 30:
            addd_damge = 1000
        else:
            addd_damge = 0
        target.take_damage(self.damage + addd_damge)