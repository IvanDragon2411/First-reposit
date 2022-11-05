class Charecter:
    name=''
    health=100
    damage=1
    defence=0
    live=True

    def __init__(self, name='', health=100, damage=1, defence=0, live=True):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.live = live
    def __str__(self):
        return f'== {self.name} \n'\
               f'HP {self.health} \n'\
               f'DMG {self.damage} \n'\
               f'def {self.defence} \n'\
               f'is alive {self.live} \n'\

    def take_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)

    def is_alive(self):
        if self.health <= 0:
            self.live = False
        else:
            self.live = True