import random
from examc import Person
from examc import Is_dead
from examc import Depresia
from examc import Bankrot
from examc import Action
from examc import Work
from examc import Rest


humans = [Person(name='Вася', money=2, mood=100, health=100, live=True),Person(name='Тарас', money=30, mood=85, health=90, live=True),Person(name='Андрей', money=5, mood=45, health=90, live=True)]

actV = [Work(money=random.randint(30, 50), mood=random.randint(-20, -10),health=random.randint(-10, -3)), Rest(money=random.randint(-25, 0), mood=random.randint(15, 20), health=random.randint(2, 7))]
actT = [Work(money=random.randint(50, 65), mood=random.randint(-30, -10),health=random.randint(-10, -3)), Rest(money=random.randint(-50, -25), mood=random.randint(30, 50),health=random.randint(5, 7))]
actA = [Work(money=random.randint(30, 50), mood=random.randint(-20, -10),health=random.randint(-10, -3)), Rest(money=random.randint(3, 10), mood=random.randint(0, 10), health=random.randint(-5, 7))]


while humans[0].live == True or humans[1].live == True or humans[2].live == True:

    try:
        print(humans[0])
    except IndexError:
        print('С Васей чото случилось')
    try:
        humans[0].do(actV[0])
    except Bankrot:
        print('Человек банкрот')
        humans[0].live = False
    except Depresia:
        print('У чела депресия')
        humans[0].live = False
    except Is_dead:
        print('Человек скончялся')
        humans[0].live = False
    except IndexError:
        print('Вася не пришол в офис, с ним явно что-то случилось')

    try:
        humans[0].do(actV[1])
    except Bankrot:
        print('Человек банкрот')
        humans[0].live = False
    except Depresia:
        print('У чела депресия')
        humans[0].live = False
    except Is_dead:
        print('Человек скончялся')
        humans[0].live = False
    except IndexError:
        print('Вася не гулял сегодня')

    try:
        print(humans[0])
    except IndexError:
        print('С Васей чото случилось')

    try:
        print(humans[1])
    except IndexError:
        print('С Тарасом чото случилось')
    try:
        humans[1].do(actT[0])
    except Bankrot:
        print('Человек банкрот')
        humans[1].live = False
    except Depresia:
        print('У чела депресия')
        humans[1].live = False
    except Is_dead:
        print('Человек скончялся')
        humans[1].live = False
    except IndexError:
        print('Тарас не пришол на работу, уволен')

    try:
        humans[1].do(actT[1])
    except Bankrot:
        print('Человек банкрот')
        humans[1].live = False
    except Depresia:
        print('У чела депресия')
        humans[1].live = False
    except Is_dead:
        print('Человек скончялся')
        humans[1].live = False
    except IndexError:
        print('Тарас не пошол тусить')

    try:
        print(humans[1])
    except IndexError:
        print('С Тарасом чото случилось')

    try:
        print(humans[2])
    except IndexError:
        print('С Андрем чото случилось')
    try:
        humans[2].do(actA[0])
    except Bankrot:
        print('Человек банкрот')
        humans[2].live = False
    except Depresia:
        print('У чела депресия')
        humans[2].live = False
    except Is_dead:
        print('Человек скончялся')
        humans[2].live = False
    except IndexError:
        print('Андрей не пришол на роботу')

    try:
        humans[2].do(actA[1])
    except Bankrot:
        print('Человек банкрот')
        humans[2].live = False
    except Depresia:
        print('У чела депресия')
        humans[2].live = False
    except Is_dead:
        print('Человек скончялся')
        humans[2].live = False
    except IndexError:
        print('Андрей не пришол к братве')

    try:
        print(humans[2])
    except IndexError:
        print('С Андрем чото случилось')

