import random

class Is_dead(Exception):
    def __init__(self, message='Человек здох!'):
        Exception.__init__(self, message)

class Depresia(Exception):
    def __init__(self, message='У человека дипресия!'):
        Exception.__init__(self, message)

class Bankrot(Exception):
    def __init__(self, message='Человек банкрот!'):
        Exception.__init__(self, message)

class Action:
    name = ''
    money = 0
    mood = 100
    health = 100

    def __init__(self, name='', money=0, mood=100, health=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.health = health

class Work(Action):

    def __init__(self, name='', money=0, mood=100, health=100):
        Action.__init__(self, name, money, mood, health )

class Rest(Action):

    def __init__(self, name='', money=0, mood=100, health=100):
        Action.__init__(self, name, money, mood, health)

class Person:
    name = ''
    money = 0
    mood = 100
    health = 100
    live = True

    def __init__(self, name='', money=0, mood=100, health=100, live=1):
        self.name = name
        self.money = money
        self.mood = mood
        self.health = health
        self.live = live


    def __str__(self):
        return f'Имя = {self.name}\nКапитал = {self.money}\n' \
               f'Настроение = {self.mood}\n' \
               f'Здорове = {self.health}\n'\
               f'Есле здесь написано False, значит обект здох и все расщоты с ним теоритичиские = {self.live}\n'

    def change_state(self, money, mood, health):

        if money < 0:
            self.money = self.money - abs(money)
        else:
            self.money = self.money + money
        if mood < 0:
            self.mood = self.mood - abs(mood)
        else:
            self.mood = self.mood + mood
        if health < 0:
            self.health = self.health - abs(health)
        else:
            self.health = self.health + health

        if self.money < 0:
            raise Bankrot
        else:
            pass
        if self.mood < 0:
            raise Depresia
        else:
            pass
        if self.health < 0:
            raise Is_dead
        else:
            pass

    def do(self, a):
        if a.money < 0:
            self.money = self.money - abs(a.money)
        else:
            self.money = self.money + a.money
        if a.mood < 0:
            self.mood = self.mood - abs(a.mood)
        else:
            self.mood = self.mood + a.mood
        if a.health < 0:
            self.health = self.health - abs(a.health)
        else:
            self.health = self.health + a.health

        if a == Work and a.mood >= 90:
            self.money = self.money + a.money / 100 * 10
        else:
            pass

        if a == Rest and a.health <= 40:
            self.mood = self.mood - a.mood / 100 * 20
        else:
            pass


        if self.money < 0:
            raise Bankrot
        else:
            pass
        if self.mood < 0:
            raise Depresia
        else:
            pass
        if self.health < 0:
            raise Is_dead
        else:
            pass








