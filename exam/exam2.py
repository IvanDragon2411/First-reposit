import random
from examc import Person
from examc import Is_dead
from examc import Depresia
from examc import Bankrot


#human1 = Person(name='Вася', money=2, mood=100, health=100)
#human2 = Person(name='Тарас', money=30, mood=85, health=90)
#human3 = Person(name='Андрей', money=5, mood=45, health=90)

humans = [Person(name='Вася', money=2, mood=100, health=100),Person(name='Тарас', money=30, mood=85, health=90),Person(name='Андрей', money=5, mood=45, health=90)]


while humans != None:
    print(humans[0])
    try:
        humans[0].change_state(money=random.randint(30, 50), mood=random.randint(-20, -10), health=random.randint(-10, -3))
    except Bankrot:
        print('Человек банкрот')
        humans.pop(0)
    except Depresia:
        print('У чела депресия')
        humans.pop(0)
    except Is_dead:
        print('Человек скончялся')
        humans.pop(0)
    print(humans[0])
    try:
        humans[0].change_state(money=random.randint(-25, 0), mood=random.randint(15, 20), health=random.randint(2, 7))
    except Bankrot:
        print('Человек банкрот')
        humans.pop(0)
    except Depresia:
        print('У чела депресия')
        humans.pop(0)
    except Is_dead:
        print('Человек скончялся')
        humans.pop(0)



    print(humans[1])
    try:
        humans[1].change_state(money=random.randint(50, 100), mood=random.randint(-20, -10),
                               health=random.randint(-10, -3))
    except Bankrot:
        print('Человек банкрот')
        humans.pop(1)
    except Depresia:
        print('У чела депресия')
        humans.pop(1)
    except Is_dead:
        print('Человек скончялся')
        humans.pop(1)
    print(humans[1])
    try:
        humans[1].change_state(money=random.randint(-50, -25), mood=random.randint(30, 50),health=random.randint(5, 12))
    except Bankrot:
        print('Человек банкрот')
        humans.pop(1)
    except Depresia:
        print('У чела депресия')
        humans.pop(1)
    except Is_dead:
        print('Человек скончялся')
        humans.pop(1)
    print(humans[1])







    print(humans[2])
    try:
        humans[2].change_state(money=random.randint(30, 50), mood=random.randint(-20, -10),health=random.randint(-10, -3))
    except Bankrot:
        print('Человек банкрот')
        humans.pop(2)
    except Depresia:
        print('У чела депресия')
        humans.pop(2)
    except Is_dead:
        print('Человек скончялся')
        humans.pop(2)
    print(humans[2])



    try:
        humans[2].change_state(money=random.randint(3, 10), mood=random.randint(0, 10),health=random.randint(-5, 7))
    except Bankrot:
        print('Человек банкрот')
        humans.pop(2)
    except Depresia:
        print('У чела депресия')
        humans.pop(2)
    except Is_dead:
        print('Человек скончялся')
        humans.pop(2)





















