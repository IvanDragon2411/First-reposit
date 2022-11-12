from Fight.Charter import Charecter
import random
class Ninja(Charecter):

    def __init__(self, name='', health=100, damage=1, defense=1000, live=True):
        Charecter.__init__(self, name, health, damage, defense, live)

    def take_damage(self, damage):
        if random.randint(1, 100) <= 20:
            self.health -= max(damage - damage, 0)
        else:
            self.health -= max(damage, 0)